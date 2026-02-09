# Flipper Zero + ESP32 App Package

This repository is now a **clean, app-first package** for people who have:
- Flipper Zero (standard)
- ESP32 module/board

It replaces the previous starter content and focuses on practical, legal, owner-authorized projects.

## What this package gives you

- A structured `apps/` workspace for Flipper and ESP32 projects
- Ready-to-run ESP32 app templates (Arduino + PlatformIO + MicroPython)
- Flipper workflow notes for IR/RFID/NFC/Sub-GHz/GPIO/BLE usage
- Scripts to:
  - generate an app catalog
  - validate package integrity
  - export/sync to your SD card or workspace

## App-focused structure

- `apps/flipper/` → Flipper-side app notes/workflows/toolbox docs
- `apps/esp32/` → ESP32 projects and firmware templates
- `scripts/` → package management scripts
- `docs/` → generated catalog and capability matrix

## Capability matrix (high-level)

You can build projects around:
- Device inventory & tagging
- Infrared remote learning and organization
- NFC / RFID cataloging
- BLE beacon logging
- GPIO diagnostics
- UART bridge tools (Flipper ⇄ ESP32 ⇄ PC)
- Sensor dashboards (ESP32)
- Data logger apps (temperature, humidity, light, motion)
- Wi-Fi telemetry for your own network devices
- OTA update workflows for your own ESP32 nodes

## Quick start

```bash
python3 scripts/validate_package.py
python3 scripts/build_catalog.py
bash scripts/export_package.sh ./out
```

## Safety

Use this only on devices, cards, keys, networks, and systems you own or are explicitly authorized to test.
