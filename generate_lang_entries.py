import sys
import os
import argparse

# Add 'src/' to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from net.reconhalcyon.toolkit.generators.lang_entries import generate_lang_entries
from net.reconhalcyon.toolkit.config_loader import load_config_with_defaults

# Placeholder Fore class in case fun_mode is disabled
class DummyFore:
    RED = GREEN = YELLOW = CYAN = RESET = ''

# Pre-init Fore in case config is not yet loaded
Fore = DummyFore

def main():
    parser = argparse.ArgumentParser(description="Generate lang entries from mod registry.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing to file")
    parser.add_argument("--only-show", action="store_true", help="Only show lang keys")
    parser.add_argument("--csv", action="store_true", help="Export result to CSV")
    parser.add_argument("--output-file", help="Lang output file override")
    parser.add_argument("--csv-output", help="CSV export path override")
    parser.add_argument("--log-dir", help="Log directory override")
    parser.add_argument("--check-config", action="store_true", help="Validate config and exit")
    parser.add_argument("--config", default="toolkit_config.json", help="Toolkit config path")

    args = parser.parse_args()
    config = load_config_with_defaults(args, config_path=args.config)

    # Handle color mode based on fun_mode
    global Fore
    if config.get("fun_mode", True):
        from colorama import init, Fore as ColorFore
        init(autoreset=True)
        Fore = ColorFore

    # Apply default fallbacks
    args.output_file = args.output_file or config["default_output_paths"]["lang_output"]
    args.csv_output = args.csv_output or config["default_output_paths"]["csv_output"]
    args.log_dir = args.log_dir or config["default_output_paths"]["log_dir"]

    if not hasattr(args, "dry_run") or args.dry_run is None:
        args.dry_run = config.get("default_dry_run", False)
    if not hasattr(args, "csv") or args.csv is None:
        args.csv = config.get("default_csv_export", False)

    print(Fore.CYAN + "[~] Running lang entry generator...")
    generate_lang_entries(config_path=args.config, cli_args=args)

if __name__ == "__main__":
    main()
