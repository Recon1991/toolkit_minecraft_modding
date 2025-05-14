import os
from colorama import Fore, Style, init as colorama_init

# Initialize only if fun_mode is active
def setup_logger(fun_mode=True):
    if fun_mode:
        colorama_init(autoreset=True)

    def style(msg, color):
        return f"{color}{msg}{Style.RESET_ALL}" if fun_mode else msg

    return {
        "info": lambda msg: print(style(f"[~] {msg}", Fore.CYAN)),
        "success": lambda msg: print(style(f"[✓] {msg}", Fore.GREEN)),
        "warning": lambda msg: print(style(f"[!] {msg}", Fore.YELLOW)),
        "error": lambda msg: print(style(f"[✗] {msg}", Fore.RED)),
        "plain": print
    }
