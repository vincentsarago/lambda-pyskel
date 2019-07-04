"""Lambda_pyskel.scripts.cli."""

import os
import shutil

import oyaml as yaml
import click

from lambda_pyskel import version


@click.command(short_help="Create new python AWS Lambda skeleton")
@click.version_option(version=version, message="%(version)s")
@click.argument("name", type=str, nargs=1)
@click.option(
    "--template",
    type=click.Choice(["simple", "rasterio", "gdal"]),
    default="simple",
    help="Use specific template (default: 'simple')",
)
@click.option(
    "--serverless-toolkit",
    type=click.Choice(["kes", "serverless"]),
    help="Add deployement toolkit",
)
def create(name, template, serverless_toolkit):
    """Create new python AWS Lambda skeleton."""
    template_dir = os.path.join(os.path.dirname(__file__), f"../templates/{template}")

    shutil.copytree(template_dir, name)

    if serverless_toolkit:
        toolkit_dir = os.path.join(
            os.path.dirname(__file__), f"../templates/toolkits/{serverless_toolkit}"
        )
        for item in os.listdir(toolkit_dir):
            s = os.path.join(toolkit_dir, item)
            d = os.path.join(name, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

        if template == "gdal":
            if serverless_toolkit == "serverless":
                config_file = os.path.join(name, f"serverless.yml")
                with open(config_file, "r+") as f:
                    d = yaml.load(f.read())
                    d["provider"].update(
                        {"environment": {"GDAL_DATA": "/var/task/share/gdal"}}
                    )
                    f.seek(0)
                    f.write(yaml.dump(d, default_flow_style=False))
            if serverless_toolkit == "kes":
                config_file = os.path.join(name, f".kes/config.yml")
                with open(config_file, "r+") as f:
                    d = yaml.load(f.read())
                    d["default"]["lambdas"]["pyskel"].update(
                        {"envs": {"GDAL_DATA": "/var/task/share/gdal"}}
                    )
                    f.seek(0)
                    f.write(yaml.dump(d, default_flow_style=False))

    new_dir = name
    name = name.replace("-", "_")
    for root, dirs, files in os.walk(new_dir):
        if root.endswith("pyskel"):
            shutil.move(root, root.replace("pyskel", name))

    for root, dirs, files in os.walk(new_dir):
        for filename in files:
            if filename.endswith(".pyc"):
                continue
            with open(f"{root}/{filename}", "r", encoding="utf-8") as f:
                s = f.read().replace("pyskel", name)

            with open(f"{root}/{filename}", "w", encoding="utf-8") as f:
                f.write(s)
