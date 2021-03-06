"""tests lambda_pyskel.cli."""

import json

import oyaml as yaml
from click.testing import CliRunner

from lambda_pyskel.scripts.cli import create


def test_create():
    """Test the create function"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(create, ["myfunction"])
        with open("myfunction/README.md", "r") as f:
            assert f.read().splitlines()[0] == "# myfunction"
        assert not result.exception
        assert result.exit_code == 0


def test_create_toolkit():
    """Test the create function with toolkit option"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(create, ["myfunction", "--serverless-toolkit", "kes"])
        with open("myfunction/package.json", "r") as f:
            assert json.loads(f.read())["devDependencies"].get("kes")
        assert not result.exception
        assert result.exit_code == 0


def test_create_toolkit_gdal():
    """Test the create function with toolkit option"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            create,
            ["myfunction", "--serverless-toolkit", "serverless", "--template", "gdal"],
        )
        with open("myfunction/serverless.yml", "r") as f:
            d = yaml.load(f.read())
            assert d["provider"]["environment"] == {"GDAL_DATA": "/var/task/share/gdal"}
        assert not result.exception
        assert result.exit_code == 0

        result = runner.invoke(
            create,
            ["myfunctiongdal", "--serverless-toolkit", "kes", "--template", "gdal"],
        )
        with open("myfunctiongdal/.kes/config.yml", "r") as f:
            d = yaml.load(f.read())
            assert d["default"]["lambdas"]["myfunctiongdal"]["envs"] == {
                "GDAL_DATA": "/var/task/share/gdal"
            }
        assert not result.exception
        assert result.exit_code == 0
