# Scripts in this package

- `scripts/build_catalog.py`
  - Scans `apps/` and generates `docs/app_catalog.json`.
  - Includes app path, group (`flipper`/`esp32`), and file size.

- `scripts/validate_package.py`
  - Verifies required app/package files exist and are non-empty.
  - Returns non-zero on failures.

- `scripts/export_package.sh`
  - Exports `apps/`, `README.md`, and `docs/` into an output directory.
  - Useful for creating a deployable package copy.
