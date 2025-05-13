import sys
import os
import argparse
from colorama import init, Fore

# Ensure src is in the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from net.reconhalcyon.toolkit.generators.item_entries import generate_item_entries
from net.reconhalcyon.toolkit.generators.lang_entries import generate_lang_entries

init(autoreset=True)

def run_item_generator(args):
    if not os.path.exists(args.input):
        print(Fore.RED + f"[!] Input file not found: {args.input}")
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
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

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(Fore.GREEN + f"[✓] Wrote item output to {args.output}")
    else:
        print(output)

def run_lang_generator(args):
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
    lang_parser.add_argument("--config", default="lang_config.json", help="Path to config JSON file")
    lang_parser.set_defaults(func=run_lang_generator)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    args.func(args)

if __name__ == "__main__":
    main()
