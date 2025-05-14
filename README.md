# Recon Modding Toolkit

This toolkit provides a modular, version-aware Python system for generating Java item entries, lang files, and other Minecraft mod data. It's designed to integrate directly into your mod workspace, support multiple Minecraft versions, and allow clean automation from the command line.

---

## 🧭 Project Structure

```
src/net/reconhalcyon/toolkit/
├── generators/
│   ├── item_entries.py         # Generates item + ModItems Java entries
│   └── lang_entries.py         # Extracts lang keys from registry code
├── commands/
│   └── doctor.py               # Toolkit self-check (paths, config, templates)
├── logger.py                   # Emoji + colorized output helper
├── config_loader.py            # Merges CLI args with toolkit_config.json
```

Top-level CLI tools:
```
generate_item_entries.py        # CLI for generating item class entries
generate_lang_entries.py        # CLI for generating lang entries
toolkit_cli.py                  # Unified CLI entry point
```

Config file:
```
toolkit_config.json             # Controls output paths, flags, toggles
```

---

## 🖥 CLI Usage

### ✅ Generate Item Entries
```bash
python generate_item_entries.py --input fishNames.txt --class FishItems --mcver 1.21.1
```

### ✅ Generate Lang File
```bash
python generate_lang_entries.py --config toolkit_config.json --dry-run --csv
```

### ✅ Use Unified CLI
```bash
python toolkit_cli.py generate-items --input fishNames.txt --class FishItems
python toolkit_cli.py generate-lang --dry-run
python toolkit_cli.py doctor
```

---

## ⚙️ Configuration: `toolkit_config.json`

Example fields:
```json
{
  "fun_mode": true,
  "enable_sound": true,
  "default_dry_run": false,
  "default_output_paths": {
    "item_output": "generated/fish_entries.java",
    "lang_output": "generated/lang/en_us.json",
    "csv_output": "generated/lang_export.csv",
    "log_dir": "logs/toolkit"
  }
}
```

This file supports all CLI tools and allows shared defaults across scripts.

---

## 🧠 Design Philosophy

| Layer       | File(s)                           | Role                          |
|-------------|-----------------------------------|-------------------------------|
| Logic       | `item_entries.py`, `lang_entries.py` | Stateless core generation     |
| CLI         | `generate_*.py`, `toolkit_cli.py` | CLI-facing execution layer    |
| Utilities   | `logger.py`, `config_loader.py`   | Shared formatting + config    |
| Commands    | `doctor.py`                       | Internal command logic        |

This structure ensures that logic is reusable, CLIs are simple, and configuration is centralized.

---

## 📦 Templates

Templates for version-aware generation live in:
```
version_templates/<mcver>/
├── item_entry.j2
├── moditems_entry.j2
```

These Jinja2 templates allow flexible formatting per Minecraft version.

---

## 🧰 Toolkit Doctor
Run a full environment check:
```bash
python toolkit_cli.py doctor
```
Checks:
- Required paths in config
- Template directory for selected version
- Registry source directories
- Output directory readiness

---

For questions or contributions, contact Recon.
