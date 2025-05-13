import sys
import os
import argparse
from colorama import init, Fore, Style

# Make 'src/' discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from net.reconhalcyon.toolkit.generators.item_entries import generate_item_entries

init(autoreset=True)

def main():
    print(Fore.CYAN + "[*] Starting item entry generation...")

    parser = argparse.ArgumentParser(description="Generate item and ModItems Java declarations.")
    parser.add_argument("--input", required=True, help="Path to text file with item names")
    parser.add_argument("--class", dest="class_name", required=True, help="Java class name, e.g., FishItems")
    parser.add_argument("--mcver", help="Minecraft version, e.g., 1.21.1")
    parser.add_argument("--output", help="Optional output file")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(Fore.RED + f"[!] Input file not found: {args.input}")
        sys.exit(1)

    print(Fore.YELLOW + f"[-] Reading names from: {args.input}")
    with open(args.input, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    if not names:
        print(Fore.RED + "[!] No item names found in the input file.")
        sys.exit(1)

    print(Fore.YELLOW + f"[-] Generating entries for class: {args.class_name}, Minecraft version: {args.mcver or 'default'}")
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
        print(Fore.GREEN + f"[✓] Wrote output to {args.output}")
    else:
        print(Fore.CYAN + "\n[=] Output:")
        print(output)

if __name__ == "__main__":
    main()
