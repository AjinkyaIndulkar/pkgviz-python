from pathlib import Path

import click

from .engine import Engine
from .utils import get_logger

logger = get_logger()


@click.command()
@click.option(
    "-p", "--package-name", required=True, help="name of the package to visualise."
)
@click.option(
    "-o", "--output-path", required=True, help="path to save rendered visualisation."
)
def main(package_name: str, output_path: str):
    """Package Visualiser CLI."""
    logger.info(f"constructing visualisation for '{package_name}' package...")
    engine_client = Engine(
        package_name=package_name, format=Path(output_path).suffix.replace(".", "")
    )

    engine_client.construct()
    engine_client.draw()
    engine_client.save(output_path)

    logger.info("job complete.")
