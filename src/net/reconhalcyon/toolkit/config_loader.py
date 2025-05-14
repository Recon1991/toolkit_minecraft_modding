import os
import json
from argparse import Namespace

DEFAULTS = {
    "fun_mode": True,
    "enable_sound": True,
    "default_dry_run": False,
    "default_csv_export": False,
    "project_namespace": "hawaiinei",
    "default_output_paths": {
        "item_output": "generated/fish_entries.java",
        "lang_output": "generated/lang/en_us.json",
        "csv_output": "generated/lang_export.csv",
        "log_dir": "logs/toolkit"
    }
}

def load_config_with_defaults(cli_args: Namespace, config_path: str = "toolkit_config.json") -> dict:
    config = {}

    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

    # Merge top-level defaults
    merged = {**DEFAULTS, **config}

    # Merge nested output paths
    merged["default_output_paths"] = {
        **DEFAULTS["default_output_paths"],
        **config.get("default_output_paths", {})
    }

    # Inject CLI overrides if present
    if hasattr(cli_args, "output_file") and cli_args.output_file:
        merged["default_output_paths"]["lang_output"] = cli_args.output_file

    if hasattr(cli_args, "csv_output") and cli_args.csv_output:
        merged["default_output_paths"]["csv_output"] = cli_args.csv_output

    if hasattr(cli_args, "log_dir") and cli_args.log_dir:
        merged["default_output_paths"]["log_dir"] = cli_args.log_dir

    return merged
