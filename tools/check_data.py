#!/usr/bin/env python3
"""Validate _data/*.yml. Run before pushing: python3 tools/check_data.py"""
import sys, glob, os, yaml
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ok = True
def err(m):
    global ok; ok = False; print("ERROR:", m)
data = {}
for f in sorted(glob.glob(os.path.join(root, "_data", "*.yml"))):
    try: data[os.path.basename(f)[:-4]] = yaml.safe_load(open(f, encoding="utf-8"))
    except Exception as e: err(f"{os.path.basename(f)} does not parse: {e}")
P, V, T = data.get("publications", []), data.get("venues", {}), data.get("themes", [])
topics = {t["key"] for t in T} | {"other"}
ids = set()
for p in P:
    for k in ("id", "title", "authors", "year", "status", "topics"):
        if k not in p: err(f"publication missing {k}: {p.get('title')}")
    if p.get("id") in ids: err(f"duplicate id {p['id']}")
    ids.add(p.get("id"))
    if p.get("status") not in ("accepted", "workshop", "preprint"): err(f"bad status: {p.get('title')}")
    if p.get("status") == "accepted" and p.get("venue") not in V: err(f"unknown venue '{p.get('venue')}': {p.get('title')}")
    for t in p.get("topics", []):
        if t not in topics: err(f"unknown topic '{t}': {p.get('title')}")
    if not any("Mitliagkas" in a for a in p.get("authors", [])): err(f"no I. Mitliagkas in authors: {p.get('title')}")
for n in data.get("news", []):
    if not isinstance(n, dict) or "date" not in n or "text" not in n: err(f"bad news item: {n}")
people = data.get("people", {})
for g in ("current", "alumni"):
    for x in people.get(g, []):
        if x.get("photo") and not os.path.exists(os.path.join(root, "images", x["photo"])): err(f"missing photo {x['photo']}")
print("data OK" if ok else "data has errors")
sys.exit(0 if ok else 1)
