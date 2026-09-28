#!/usr/bin/env sh
set -eu
python3 -m unittest discover -s testler -p 'test_*.py' -v
if command -v node >/dev/null 2>&1; then
  find ortak ana-tema sayfalar docs -type f -name '*.js' -exec node --check {} \;
  node testler/test_loader_url.js
else
  echo 'UYARI: node bulunamadı; JavaScript kontrolleri çalıştırılamadı.' >&2
  exit 1
fi
