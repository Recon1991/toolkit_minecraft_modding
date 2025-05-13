import sys
import os
import argparse
from colorama import init, Fore

# Add 'src/' to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from net.reconhalcyon.toolkit.generators.lang_entries import generate_lang_entries

init(autoreset=True)

def main():
    print(Fore.CYAN + "[*] Starting lang entry generation...")

    parser = argparse.ArgumentParser(description="Generate and merge Minecraft lang entries.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing to file.")
    parser.add_argument("--only-show", action="store_true", help="Only show registry-derived lang keys.")
    parser.add_argument("--csv", action="store_true", help="Export results as CSV.")
    parser.add_argument("--output-file", help="Override output file path.")
    parser.add_argument("--csv-output", help="Path to write CSV export.")
    parser.add_argument("--log-dir", help="Directory for log files.")
    parser.add_argument("--check-config", action="store_true", help="Validate config and exit.")
    parser.add_argument("--config", default="lang_config.json", help="Path to config JSON file.")

    args = parser.parse_args()
    generate_lang_entries(config_path=args.config, cli_args=args)

if __name__ == "__main__":
    main()
