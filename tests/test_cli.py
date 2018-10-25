"""tests lambda_pyskel.cli."""

from click.testing import CliRunner

from lambda_pyskel.scripts.cli import create


def test_create():
    """Test the create function"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(create, ["myfunction"])
        with open("myfunction/README.rst", "r") as f:
            assert f.read().splitlines()[0] == "myfunction"
        assert not result.exception
        assert result.exit_code == 0
