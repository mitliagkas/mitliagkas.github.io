# Updating the site

Jekyll site served by GitHub Pages from `master`. No theme, no plugins beyond
`jekyll-redirect-from`, one stylesheet (`assets/css/site.css`), one small script
(the filter on the publications page).

## Where content lives

Most content is data. Edit the YAML file; every page that uses it updates.

| What | File | Shown on |
|---|---|---|
| Publications | `_data/publications.yml` (generated, see below) | Publications, Research, Home (featured) |
| Venue names and counts | `_data/venues.yml` | Publications, CV tools |
| Research themes | `_data/themes.yml` | Home, Research, publication filters |
| Students and alumni | `_data/people.yml` | Home, Group |
| News | `_data/news.yml` | Home (latest 6), News |
| Courses | `_data/teaching.yml` | Teaching |
| Funding acknowledgements | `_data/funders.yml` | Research (end of page) |
| Photo gallery | `_data/gallery.yml` | Extracurriculars |
| Recruiting notice, nav, profile links | `_config.yml` | Home, header, footer |
| Redirects for removed files (PDFs and other non-page URLs) | `404.html` (the `MOVED` table); page URLs use `redirect_from` | Old links from other sites |

Prose pages: `index.html` (bio), `pages/*.html`, `extracurriculars.md`, course pages
(`ml-class*.md`, `ift6169-*.md`). Images go in `images/`; student photos are
400×400 `images/person-<name>.jpg`.

## Common tasks

- **New paper, or a paper accepted:** change the source, not this repository (see Publications below).
- **New student:** add to `current` in `_data/people.yml`. **Graduation:** move them to `alumni`
  with `year` and `next`, and add a news item.
- **Recruiting season over:** set `recruiting.open: false` in `_config.yml`.

## Publications

`_data/publications.yml` is generated. Do not edit it here: every update overwrites it.
The publication list is maintained in a private source together with papers under review,
which are never published here. Changes arrive as a pull request titled "Update publications",
which lists the ids added, removed or changed; review and merge it like any other.

The CV and CCV files are generated from the same private source, so the CV tools live there too.
`venues.yml`, `themes.yml` and `people.yml` stay here; those tools read them from this repository.

## Class editions and old links

Old links from other sites point into past editions of a class. To keep them working:

- **A past edition is frozen.** `ift6169-2023/` is the last edition of the original IFT 6169
  class. Never rename, move or delete a file in it; every 2018-2022 link is forwarded there.
  Fixing a typo in a PDF is fine if the file name stays the same.
- **Each new edition gets its own folder and page:** `ift6169-2027/` and `/ift6169-2027/`.
  New material never overwrites an earlier edition's files.
- **Superseded material is offered, not redirected.** When a newer edition replaces an old
  lecture, change that lecture's entries in the `MOVED` table of `404.html` from a URL to
  `{"original": "<old edition URL>", "updated": "<new edition URL>"}`. The 404 page then shows
  both and lets the reader choose. On the old edition's page, add "newer version" next to the
  lecture.
- **Optional stable link:** `/ift6169/` can redirect (with `redirect_from`) to the current
  edition. Move it to the new page each time an edition starts.
- **File names in new editions** are by topic, not lecture number:
  `ift6169-2027/notes-momentum.pdf`, `ift6169-2027/slides-momentum.pdf`. The class page and the
  PDF title give the order. The same topic keeps the same name in later editions, which makes
  matching editions easy. Existing 2023 names stay as they are.
- **If a frozen edition must be removed,** add its paths to the `MOVED` table and re-point the
  entries that targeted it.

## Checks and previews

- `python3 tools/check_data.py` validates the data files.
- Every push to a branch other than `master` runs `.github/workflows/preview.yml`: it checks the
  data, builds with the same gems as GitHub Pages, and publishes the built site to the
  `preview-site` branch.
- Local preview: `bundle install && bundle exec jekyll serve`.

## Paper ids and arXiv ids

- A paper's `id` is assigned once and never changed, even if the title changes. The CV and
  CCV (BibTeX keys) depend on it.
- Each arXiv id belongs to exactly one entry. `tools/check_data.py` fails if two entries share
  one, or if an id has a version suffix (`2012.05782`, not `2012.05782v2`).
- Papers are matched by arXiv id first and by title only when there is no arXiv id.

## Conventions

- Changes go through a branch and a pull request.
- Never commit API keys or tokens.
- Details about people are confirmed by the site owner before publishing.
