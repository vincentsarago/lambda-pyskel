"""Lambda_pyskel.scripts.cli."""

import os
import shutil

import click


@click.command(short_help="Create new python AWS Lambda skeleton")
@click.argument("name", type=str, nargs=1)
@click.option(
    "--template",
    type=click.Choice(["simple", "rasterio", "gdal"]),
    default="simple",
    help="Use specific template (default: 'simple')",
)
def create(name, template):
    """Create new python AWS Lambda skeleton."""
    template_dir = os.path.join(os.path.dirname(__file__), f"../templates/{template}")

    shutil.copytree(template_dir, name)

    new_dir = name
    name = name.replace("-", "_")
    for root, dirs, files in os.walk(new_dir):
        if root.endswith("pyskel"):
            shutil.move(root, root.replace("pyskel", name))

    for root, dirs, files in os.walk(new_dir):
        for filename in files:
            with open(f"{root}/{filename}", "r") as f:
                s = f.read().replace("pyskel", name)

            with open(f"{root}/{filename}", "w") as f:
                f.write(s)
