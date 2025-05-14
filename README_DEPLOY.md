# Recon Modding Toolkit — Deployable Package

This archive contains a self-contained copy of the **Recon Minecraft Modding Toolkit** for use inside a mod project (e.g., `hawaiinei-mod`).

---

## 📦 Included in This Package

- `src/net/reconhalcyon/toolkit/` — The full Python toolkit module
- `version_templates/` — Jinja2 templates for version-aware outputs
- `toolkit_config.json` — Default configuration file for toolkit behavior
- CLI Scripts:
    - `toolkit_cli.py` — Unified command-line interface
    - `generate_item_entries.py` — Standalone item entry generator
    - `generate_lang_entries.py` — Lang file generator

---

## 🛠 How to Install (Local Dev Mode)

### 1. Unzip into Your Mod Project

Place the contents into the root of your mod project, preserving this structure:

```
your-mod/
├── src/
│   └── net/
│       └── reconhalcyon/
│           ├── hawaiinei/        <- your mod source
│           └── toolkit/          <- this toolkit
├── version_templates/
├── toolkit_config.json
├── toolkit_cli.py
├── generate_item_entries.py
├── generate_lang_entries.py
```

### 2. Install Python Dependencies

From the project root:

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install colorama jinja2 pygame
```

---

## 🧪 Example CLI Usage

### Generate Item Entries
```bash
python toolkit_cli.py generate-items --input fishNames.txt --class FishItems --mcver 1.21.1 --output fishOutput.java
```

### Generate Lang File
```bash
python toolkit_cli.py generate-lang --config lang_config.json --dry-run --csv
```

---

## 🧩 Integration Notes

- Treat `src/` as your Python source root.
- If needed, prepend this to CLI scripts:
  ```python
  import sys, os
  sys.path.insert(0, os.path.abspath("src"))
  ```
- You can customize `toolkit_config.json` as needed for your project.

---

## ✅ Ready to Use

This setup is designed to be dropped into **any mod workspace** that uses the `net.reconhalcyon` namespace. No path rewrites needed.

For questions or updates, refer to the original repository or your internal toolkit documentation.
