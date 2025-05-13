import json
import os

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..", "config.json"))

def read_config():
    print("Looking for config.json at:", CONFIG_PATH)
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("Missing config.json.")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
