import os
import json
import random
from net.reconhalcyon.toolkit.config_loader import load_config_with_defaults
from net.reconhalcyon.toolkit.logger import setup_logger

MOODS = {
    "default": {
        "header": [
            " _____          _     _ _                         ",
            "|_   _|        | |   (_) |                        ",
            "  | | __ _  ___| |__  _| | _____  _ __ ___   __ _ ",
            "  | |/ _` |/ __| '_ \| | |/ / _ \| '_ ` _ \ / _` |",
            "  | | (_| | (__| | | | |   < (_) | | | | | | (_| |",
            "  \_/\__,_|\___|_| |_|_|_|\_\___/|_| |_| |_|\__,_|",
            "                                                 ",
            "              Tachikoma AI Companion              "
        ],
        "greeting": [
            "🤖 [BOOT] Tachikoma system link established. Initializing preflight scan...",
            "🧠 [AI-CORE] Pattern recognition engaged. Beginning file system trace.",
            "🕷️ [TRACE] Cross-referencing toolkit nodes with registry schema...",
            "💡 [SYNC] Toolkit modules pinged. Awaiting response...",
            "🔍 [PROBE] Running self-diagnostics on toolkit architecture...",
            "🧬 [NET-SCAN] Checking directory trees and template integrity..."
        ]
    },
    "chatty": {
        "header": [
            "#===============================#",
            "|  TACHIKOMA AI DIAGNOSTICS 🕷️  |",
            "#===============================#"],
        "greeting": [
            "Hiya recon~! I'm ready to check your toolkit!",
            "Warming up my sensors... let's take a look around.",
            "I love scanning! I hope everything's in place today 🕵️‍♀️",
            "Toolkit time! Zoom zoom~"
        ]
    },
    "serious": {
        "header": [
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
            "▓      SYSTEM CHECKPOINT     ▓",
            "▓     Ghost Protocol Mode    ▓",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
        ],
        "greeting": [
            "[BOOT] Tachikoma initialized. Running deep scan...",
            "[SECURE] Initial handshake complete.",
            "[TRACE] Scanning recon mod layers for readiness."
        ]
    }
}

def run_tachikoma(args):
    config = load_config_with_defaults(args, config_path=args.config)
    log = setup_logger(config.get("fun_mode", True))

    mood = config.get("tachikoma_mood", "default")
    profile = MOODS.get(mood, MOODS["default"])

    for line in profile["header"]:
        print(line)

    log["info"](random.choice(profile["greeting"]))

    # Check required paths
    checks = {
        "[PATH] Lang Output": config["default_output_paths"].get("lang_output"),
        "[PATH] CSV Export": config["default_output_paths"].get("csv_output"),
        "[PATH] Log Directory": config["default_output_paths"].get("log_dir"),
    }

    for label, path in checks.items():
        if path:
            exists = os.path.exists(path) or os.path.exists(os.path.dirname(path))
            if exists:
                log["success"](f"{label} ✅ {path}")
            else:
                log["warning"](f"{label} ⚠️ Missing or invalid path: {path}")

    # Check version templates
    template_dir = os.path.join("version_templates", config.get("mcver", "1.21.1"))
    if os.path.exists(template_dir):
        log["success"](f"[TEMPLATES] ✅ Found: {template_dir}")
    else:
        log["error"](f"[TEMPLATES] ❌ Missing versioned template directory: {template_dir}")

    # Check registry dirs from groups
    if "groups" in config:
        for group in config["groups"]:
            group_type = group.get("type")
            registry_dir = group.get("registry_dir")
            label = f"[GROUP] {group_type.capitalize()} Registry"
            if registry_dir:
                if os.path.exists(registry_dir):
                    log["success"](f"{label} ✅ {registry_dir}")
                else:
                    log["error"](f"{label} ❌ Not found: {registry_dir}")
            else:
                log["warning"](f"{label} ⚠️ No 'registry_dir' defined in config")

    log["info"]("✨ [CORE STATUS] All systems operational. Mission ready, recon.")
