from jinja2 import Environment, FileSystemLoader
from net.reconhalcyon.toolkit.utils import slugify, constantify
from net.reconhalcyon.toolkit.config import read_config
import os

def generate_item_entries(names, class_name, mcver=None):
    config = read_config()
    version = mcver or config.get("default_mcver")
    version_path = os.path.join("version_templates", version)

    if not os.path.isdir(version_path):
        raise FileNotFoundError(f"No templates for version {version} at {version_path}")

    env = Environment(loader=FileSystemLoader(version_path))
    item_template = env.get_template("item_entry.j2")
    moditems_template = env.get_template("moditems_entry.j2")

    names.sort(key=str.casefold)
    item_lines = []
    moditems_lines = []

    for name in names:
        slug = slugify(name)
        const = constantify(name)
        context = {
            "slug_name": slug,
            "const_name": const,
            "class_name": class_name
        }
        item_lines.append(item_template.render(context))
        moditems_lines.append(moditems_template.render(context))

    return item_lines, moditems_lines
