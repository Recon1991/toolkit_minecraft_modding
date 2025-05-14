import sys
import os
import argparse
from colorama import init, Fore

# Add 'src/' to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from net.reconhalcyon.toolkit.generators.item_entries import generate_item_entries
from net.reconhalcyon.toolkit.generators.lang_entries import generate_lang_entries
from net.reconhalcyon.toolkit.config_loader import load_config_with_defaults

init(autoreset=True)

def run_item_generator(args):
    config = load_config_with_defaults(args)

    input_path = args.input
    output_path = args.output or config["default_output_paths"]["item_output"]

    if not os.path.exists(input_path):
        print(Fore.RED + f"[!] Input file not found: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    if not names:
        print(Fore.RED + "[!] No item names found in the input file.")
        sys.exit(1)

    item_lines, moditems_lines = generate_item_entries(names, args.class_name, args.mcver)

    output = "\n".join([
        "// Field declarations for class file:",
        *item_lines,
        "\n// Forwarding entries for ModItems:",
        *moditems_lines
    ])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(Fore.GREEN + f"[✓] Wrote item output to {output_path}")

def run_lang_generator(args):
    config = load_config_with_defaults(args)

    # Use merged values from config
    args.output_file = args.output_file or config["default_output_paths"]["lang_output"]
    args.csv_output = args.csv_output or config["default_output_paths"]["csv_output"]
    args.log_dir = args.log_dir or config["default_output_paths"]["log_dir"]

    # Apply dry-run or CSV default if not set explicitly
    if not hasattr(args, "dry_run") or args.dry_run is None:
        args.dry_run = config.get("default_dry_run", False)
    if not hasattr(args, "csv") or args.csv is None:
        args.csv = config.get("default_csv_export", False)

    generate_lang_entries(config_path=args.config, cli_args=args)

def main():
    parser = argparse.ArgumentParser(description="Recon Minecraft Modding Master Toolkit")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Item entries command
    item_parser = subparsers.add_parser("generate-items", help="Generate Java item class and ModItems entries")
    item_parser.add_argument("--input", required=True, help="Text file with item names")
    item_parser.add_argument("--class", dest="class_name", required=True, help="Java class name, e.g., FishItems")
    item_parser.add_argument("--mcver", help="Minecraft version, e.g., 1.21.1")
    item_parser.add_argument("--output", help="Output file path")
    item_parser.set_defaults(func=run_item_generator)

    # Lang file generation command
    lang_parser = subparsers.add_parser("generate-lang", help="Generate lang file from registry entries")
    lang_parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing to file")
    lang_parser.add_argument("--only-show", action="store_true", help="Only show registry-derived lang keys")
    lang_parser.add_argument("--csv", action="store_true", help="Export results as CSV")
    lang_parser.add_argument("--output-file", help="Override output file path")
    lang_parser.add_argument("--csv-output", help="Path to write CSV export")
    lang_parser.add_argument("--log-dir", help="Directory for log files")
    lang_parser.add_argument("--check-config", action="store_true", help="Validate config and exit")
    lang_parser.add_argument("--config", default="toolkit_config.json", help="Path to config JSON file")
    lang_parser.set_defaults(func=run_lang_generator)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    args.func(args)

if __name__ == "__main__":
    main()
