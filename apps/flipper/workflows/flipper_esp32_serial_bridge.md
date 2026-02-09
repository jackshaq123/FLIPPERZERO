# Flipper ⇄ ESP32 Serial Bridge Workflow

## Goal
Use Flipper UART terminal to control a custom ESP32 CLI.

## Steps
1. Flash ESP32 firmware from `apps/esp32/arduino/serial_cli_bridge/`.
2. Connect UART pins with common ground.
3. Open Flipper UART app and connect at 115200 baud.
4. Send commands:
   - `help`
   - `led on`
   - `led off`
   - `status`
5. Save command notes in your session log.
