import os
import json
from net.reconhalcyon.toolkit.config_loader import load_config_with_defaults
from net.reconhalcyon.toolkit.logger import setup_logger

def run_doctor(args):
    config = load_config_with_defaults(args, config_path=args.config)
    log = setup_logger(config.get("fun_mode", True))

    log["info"]("🔍 Running toolkit health check...")

    # Check required paths
    checks = {
        "Lang Output Path": config["default_output_paths"].get("lang_output"),
        "CSV Export Path": config["default_output_paths"].get("csv_output"),
        "Log Directory": config["default_output_paths"].get("log_dir"),
    }

    for label, path in checks.items():
        if path:
            exists = os.path.exists(path) or os.path.exists(os.path.dirname(path))
            if exists:
                log["success"](f"{label} OK: {path}")
            else:
                log["warning"](f"{label} missing or parent dir not found: {path}")

    # Check version templates
    template_dir = os.path.join("version_templates", config.get("mcver", "1.21.1"))
    if os.path.exists(template_dir):
        log["success"](f"Templates found: {template_dir}")
    else:
        log["error"](f"Missing template directory: {template_dir}")

    # Check registry dirs from groups
    if "groups" in config:
        for group in config["groups"]:
            group_type = group.get("type")
            registry_dir = group.get("registry_dir")
            if registry_dir:
                if os.path.exists(registry_dir):
                    log["success"](f"{group_type.capitalize()} group directory OK: {registry_dir}")
                else:
                    log["error"](f"Missing {group_type} group directory: {registry_dir}")
            else:
                log["warning"](f"Missing 'registry_dir' for group of type '{group_type}'")

    log["info"]("✅ Toolkit health check complete.")
