#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${project_root}"

command -v node >/dev/null 2>&1 || {
  echo "Node.js is not available. Open START_HERE.html for the beginner setup steps." >&2
  exit 66
}

command -v python3 >/dev/null 2>&1 || {
  echo "Python 3 is not available. Open START_HERE.html for the beginner setup steps." >&2
  exit 66
}

python3 - <<'PY'
import sys
if not ((3, 11) <= sys.version_info[:2] <= (3, 13)):
    raise SystemExit(
        f"Python {sys.version_info.major}.{sys.version_info.minor} is not supported; "
        "use Python 3.11 through 3.13."
    )
PY

if [[ ! -x "node_modules/.bin/vite" ]]; then
  echo "First start: downloading the prototype's locked supporting components into this folder."
  npm ci
fi

echo "Preparing the local synthetic practice data."
python3 scripts/setup.py
echo "Starting the private course site. Use the Local address shown below."
echo "Keep this Terminal window open. Stop the site later with Control-C."
exec env WRANGLER_LOG_PATH=.wrangler/wrangler.log ./node_modules/.bin/vite
