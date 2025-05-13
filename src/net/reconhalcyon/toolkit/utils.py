def slugify(name: str) -> str:
    return name.lower().replace(" ", "_").replace("-", "_")

def constantify(name: str) -> str:
    return slugify(name).upper()
