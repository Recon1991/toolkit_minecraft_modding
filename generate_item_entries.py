import sys
import os
import argparse

# Add 'src/' to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from net.reconhalcyon.toolkit.generators.item_entries import generate_item_entries
from net.reconhalcyon.toolkit.config_loader import load_config_with_defaults

# Placeholder Fore class in case fun_mode is disabled
class DummyFore:
    RED = GREEN = YELLOW = CYAN = RESET = ''

# Pre-init Fore in case config is not yet loaded
Fore = DummyFore

def main():
    parser = argparse.ArgumentParser(description="Generate item class entries and ModItems forwards.")
    parser.add_argument("--input", required=True, help="Path to text file with item names")
    parser.add_argument("--class", dest="class_name", required=True, help="Java class name, e.g., FishItems")
    parser.add_argument("--mcver", help="Minecraft version string (e.g., 1.21.1)")
    parser.add_argument("--output", help="Output file path (optional)")
    parser.add_argument("--config", default="toolkit_config.json", help="Toolkit config path")

    args = parser.parse_args()
    config = load_config_with_defaults(args, config_path=args.config)

    # Handle color mode based on fun_mode
    global Fore
    if config.get("fun_mode", True):
        from colorama import init, Fore as ColorFore
        init(autoreset=True)
        Fore = ColorFore

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

    print(Fore.CYAN + "[~] Generating item and ModItems entries...")
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

if __name__ == "__main__":
    main()
