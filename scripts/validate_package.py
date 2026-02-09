#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "apps/flipper/toolbox/app_pack_index.md",
    "apps/flipper/notes/flipper_workflows.md",
    "apps/flipper/workflows/flipper_esp32_serial_bridge.md",
    "apps/esp32/arduino/serial_cli_bridge/serial_cli_bridge.ino",
    "apps/esp32/arduino/sensor_logger/sensor_logger.ino",
    "apps/esp32/platformio/esp32_status_api/platformio.ini",
    "apps/esp32/platformio/esp32_status_api/src/main.cpp",
    "apps/esp32/micropython/main.py",
    "docs/CAPABILITIES.md",
    "README.md",
]


def main() -> int:
    errors = []
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"Missing: {rel}")
        elif path.is_file() and path.stat().st_size == 0:
            errors.append(f"Empty: {rel}")

    if errors:
        print("Validation FAILED")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
