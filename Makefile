# Recon Modding Toolkit - Makefile

# Set base paths for mapping and generated output
MAPPING_DIR=src/net/reconhalcyon/toolkit/mapping
GENERATED_DIR=src/net/reconhalcyon/toolkit/generated

# 🐟 Generate item entries for FishItems
fishitems:
	python toolkit_cli.py generate-items --input $(MAPPING_DIR)/fishNames.txt --class FishItems --mcver 1.21.1 --output $(GENERATED_DIR)/FishItems.java

# 🏷 Generate lang file from registry entries
lang:
	python toolkit_cli.py generate-lang --config toolkit_config.json --csv

# 🤖 Run toolkit preflight diagnostic (Tachikoma)
tachikoma:
	python toolkit_cli.py tachikoma

# 📦 Package the toolkit (optional future target)
package:
	python package_toolkit.py

# ❓ Default help message
help:
	@echo "\nRecon Modding Toolkit Commands:"
	@echo "  make fishitems     Generate item entries for FishItems"
	@echo "  make lang          Generate lang file with CSV export"
	@echo "  make tachikoma     Run configuration + path validation"
	@echo "  make package       Build deployable zip (optional)"
	@echo "  make help          Show this help message"
