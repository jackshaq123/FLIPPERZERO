#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <output_dir>"
  exit 1
fi

OUT="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$OUT"
rsync -av --delete "$ROOT/apps/" "$OUT/apps/"
rsync -av "$ROOT/README.md" "$OUT/README.md"
rsync -av "$ROOT/docs/" "$OUT/docs/"

echo "Package exported to: $OUT"
