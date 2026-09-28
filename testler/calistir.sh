#!/usr/bin/env sh
set -eu
python3 -m unittest discover -s testler -p 'test_*.py' -v
if command -v node >/dev/null 2>&1; then
  find ortak ana-tema sayfalar pages -type f -name '*.js' -exec node --check {} \; 2>/dev/null || true
fi
