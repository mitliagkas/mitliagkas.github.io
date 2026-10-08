#!/usr/bin/env python3
"""BibTeX export from the website data (_data/publications.yml).

Needs Python 3 and PyYAML (pip install pyyaml). Run from anywhere; paths are
relative to the repository root.

Examples
  # Everything (accepted, workshop, preprint) -> publications.bib
  python3 tools/bib.py -o publications.bib

  # Only peer-reviewed papers since 2020
  python3 tools/bib.py --status accepted --since 2020 -o accepted-2020.bib

  # Papers not yet in the Canadian Common CV (accepted + workshop, not marked ccv: true),
  # with student co-authors listed in a `note` field to help with CCV's student flags
  python3 tools/bib.py --ccv-new --students -o ccv-new.bib

  # After importing a file into CCV, mark its entries as imported (adds `ccv: true`)
  python3 tools/bib.py --mark-imported ccv-new.bib

Keys are the `id` field without punctuation (e.g. mahajan2026beyondmultitokenprediction),
so they are stable across runs.
"""
import argparse, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "_data")
PUBS = os.path.join(DATA, "publications.yml")

def load(name):
    with open(os.path.join(DATA, name + ".yml"), encoding="utf-8") as f:
        return yaml.safe_load(f)

def bibkey(p):
    return re.sub(r"[^a-z0-9]", "", p["id"].lower())

# --- students -----------------------------------------------------------------
def student_matchers():
    """(surname, first initial) for every student/intern in _data/people.yml."""
    people = load("people")
    out = set()
    for group in ("current", "alumni"):
        for x in people.get(group, []):
            if x.get("role") in ("phd", "msc", "intern"):
                name = re.sub(r"\(.*?\)", "", x["name"]).split()
                out.add((name[-1].lower(), name[0][0].lower()))
    return out

def students_in(p, matchers):
    hits = []
    for a in p["authors"]:
        a2 = a.rstrip("*").strip()
        parts = a2.replace(".", ". ").split()
        if not parts: continue
        sur, ini = parts[-1].lower(), parts[0][0].lower()
        if (sur, ini) in matchers and "Mitliagkas" not in a2:
            hits.append(a2)
    return hits

# --- BibTeX -------------------------------------------------------------------
def esc(s):
    return s.replace("&", r"\&").replace("%", r"\%")

def entry(p, venues, matchers=None):
    v = venues.get(p.get("venue")) if p["status"] == "accepted" else None
    if v and v.get("type") == "journal":
        kind, where = "article", ("journal", v["name"])
    elif p["status"] == "preprint":
        kind, where = "misc", ("howpublished", p.get("venue_text") or "arXiv preprint")
    else:
        kind, where = "inproceedings", ("booktitle", v["name"] if v else p.get("venue_text", ""))
    f = [("title", "{" + esc(p["title"]) + "}"),
         ("author", " and ".join(a.rstrip("*").strip() for a in p["authors"])),
         ("year", str(p["year"])), where]
    if p.get("arxiv"):
        f += [("eprint", p["arxiv"]), ("archiveprefix", "arXiv")]
    url = p.get("url") or (f"https://arxiv.org/abs/{p['arxiv']}" if p.get("arxiv") else None)
    if url: f.append(("url", url))
    notes = []
    if p.get("highlight"): notes.append(p["highlight"].capitalize() + " presentation")
    if p.get("note"): notes.append(p["note"])
    if matchers is not None:
        s = students_in(p, matchers)
        if s: notes.append("Student co-authors: " + ", ".join(s))
    if notes: f.append(("note", "; ".join(notes)))
    body = ",\n".join(f"  {k} = {{{val}}}" for k, val in f if val)
    return f"@{kind}{{{bibkey(p)},\n{body}\n}}\n"

def select(pubs, status, since, ccv_new):
    out = []
    for p in pubs:
        if status and p["status"] not in status: continue
        if since and (p.get("year") or 0) < since: continue
        if ccv_new and (p.get("ccv") or p["status"] == "preprint"): continue
        out.append(p)
    return out

# --- marking entries as imported into CCV -------------------------------------
def mark_imported(bibfile):
    keys = set(re.findall(r"@\w+\{([^,]+),", open(bibfile, encoding="utf-8").read()))
    pubs = load("publications")
    ids = {bibkey(p): p["id"] for p in pubs if not p.get("ccv")}
    todo = [ids[k] for k in keys if k in ids]
    text = open(PUBS, encoding="utf-8").read()
    for pid in todo:
        start = text.index(f"- id: {pid}\n")
        nxt = text.find("\n- id: ", start + 1)
        nxt = len(text) if nxt == -1 else nxt + 1
        block = text[start:nxt]
        if "\n  ccv:" not in block:
            block = block.rstrip("\n") + "\n  ccv: true\n"
            text = text[:start] + block + text[nxt:]
    open(PUBS, "w", encoding="utf-8").write(text)
    yaml.safe_load(open(PUBS, encoding="utf-8"))  # still valid YAML
    print(f"marked {len(todo)} of {len(keys)} entries as imported into CCV")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-o", "--output", help="output file (default: stdout)")
    ap.add_argument("--status", help="comma-separated: accepted,workshop,preprint (default: all)")
    ap.add_argument("--since", type=int, help="only papers from this year on")
    ap.add_argument("--ccv-new", action="store_true", help="accepted + workshop papers not marked ccv: true")
    ap.add_argument("--students", action="store_true", help="add a note listing student co-authors (from people.yml)")
    ap.add_argument("--mark-imported", metavar="BIBFILE", help="set ccv: true for every entry in BIBFILE, then exit")
    a = ap.parse_args()
    if a.mark_imported:
        return mark_imported(a.mark_imported)
    pubs, venues = load("publications"), load("venues")
    status = set(a.status.split(",")) if a.status else None
    sel = select(pubs, status, a.since, a.ccv_new)
    matchers = student_matchers() if a.students else None
    head = "% Generated by tools/bib.py from _data/publications.yml. Edit the data file, not this file.\n\n"
    text = head + "\n".join(entry(p, venues, matchers) for p in sel)
    if a.output:
        open(a.output, "w", encoding="utf-8").write(text)
        print(f"wrote {len(sel)} entries to {a.output}", file=sys.stderr)
    else:
        sys.stdout.write(text)

if __name__ == "__main__":
    main()
