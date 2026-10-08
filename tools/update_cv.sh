#!/usr/bin/env bash
# Regenerate CV material from the website data into an Overleaf clone.
#   tools/update_cv.sh ~/workspace/claude/IoannisCV
# Then, in the clone: compile, check, git commit, git push.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
cv="${1:?usage: tools/update_cv.sh PATH_TO_OVERLEAF_CLONE}"
[ -f "$cv/main.tex" ] || { echo "no main.tex in $cv" >&2; exit 1; }
python3 "$here/tools/check_data.py"
python3 "$here/tools/cv.py" "$cv"
echo
echo "Next, in $cv:"
echo "  compile main.tex and short/short.tex, check the PDFs, then"
echo "  git add main.tex short/short.tex pubs-*.tex pubsummary.tex ccv-new.bib && git commit -m 'Update publications' && git push"
