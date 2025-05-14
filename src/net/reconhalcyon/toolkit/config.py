import json
import os

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..", "toolkit_config.json"))

def read_config():
    print("Looking for toolkit_config.json at:", CONFIG_PATH)
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("Missing toolkit_config.json.")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
