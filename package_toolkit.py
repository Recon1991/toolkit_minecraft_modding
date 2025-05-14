import os
import zipfile
from datetime import datetime

# Output
ZIP_NAME = f"recon_toolkit_deploy_{datetime.now().strftime('%Y%m%d')}.zip"

# Paths to include
INCLUDE = [
    "src/net/reconhalcyon/toolkit",       # core Python package
    "version_templates",                  # all version-aware templates
    "toolkit_config.json",                # config file
    "toolkit_cli.py",                     # master CLI
    "generate_lang_entries.py",           # Generator for lang en_us
    "generate_item_entries.py",           # Generator for item entries (tooltips, shift_prompt, modItems, etc.)
    "README_DEPLOY.md"
]

def zip_toolkit():
    with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
        for path in INCLUDE:
            if not os.path.exists(path):
                print(f"[!] Skipping missing: {path}")
                continue

            if os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arc_path = os.path.relpath(full_path)
                        zipf.write(full_path, arcname=arc_path)
            else:
                zipf.write(path)

    print(f"[✓] Created deployable toolkit ZIP: {ZIP_NAME}")

if __name__ == "__main__":
    zip_toolkit()
