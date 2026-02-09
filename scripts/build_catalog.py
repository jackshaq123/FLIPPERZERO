#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"
OUT = ROOT / "docs" / "app_catalog.json"


def classify(path: Path) -> str:
    p = path.as_posix()
    if "/flipper/" in p:
        return "flipper"
    if "/esp32/" in p:
        return "esp32"
    return "other"


def main() -> None:
    files = []
    for path in sorted(APPS.rglob("*")):
        if path.is_file():
            rel = path.relative_to(ROOT).as_posix()
            files.append(
                {
                    "path": rel,
                    "group": classify(path),
                    "bytes": path.stat().st_size,
                }
            )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"files": files}, indent=2) + "\n", encoding="utf-8")
    print(f"catalog entries: {len(files)} -> {OUT}")


if __name__ == "__main__":
    main()
