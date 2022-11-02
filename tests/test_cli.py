import pytest
from click.testing import CliRunner

from pkgviz.cli import main


@pytest.fixture(scope="function")
def runner(request):
    """Fixture for CLI runner."""
    return CliRunner()


def test_cli_help(runner):
    """Tests the help command of Shoeblender CLI."""
    # invoke help command
    result = runner.invoke(main, ["--help"])

    assert not result.exception
    assert "Package Visualiser CLI." in result.output
    assert result.exit_code == 0


def test_cli_run(runner, tmp_path):
    """Tests pkgviz CLI run."""

    output_path = tmp_path / "output.svg"
    runner.invoke(main, ["-p", "math", "-o", str(output_path)])

    assert output_path.exists()
