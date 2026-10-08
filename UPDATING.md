# Updating the site

Jekyll site served by GitHub Pages (branch `master`). Content is hand-written HTML/Markdown.

| What | Where |
|---|---|
| News, students/postdocs, past students, teaching, funding | `index.html` (sections marked by `<h2>`) |
| Publications | `_includes/biblio-new.html` (recent, TeX4ht output) and `_includes/biblio.html`, `biblio_*.html` (older); source `biblio/biblio.bib` |
| Course pages | `ml-class*.md`, `dl-theory-class*.md`, `ift*` folders |
| Extracurriculars / photos | `photography.md`, `_includes/gallery.html` (static Flickr URLs) |
| Images of people | `images/person-*.jpg` |
| CV | `cv.pdf` |

## Conventions
- Newest items first in News and in publication lists.
- Changes go through a branch and a pull request; do not push to `master` directly.
- Never commit API keys or tokens. The old Flickr block was removed from `_config.yml`; the photo gallery is static and does not need it.
- Details about people (students, placements) are confirmed by the site owner before publishing.
