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

Prose pages: `index.html` (bio), `pages/*.html`, `extracurriculars.md`, course pages
(`ml-class*.md`, `dl-theory-class*.md`). Images go in `images/`; student photos are
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
