from importlib import import_module
from pathlib import Path

import graphviz

from .types import Node
from .utils import construct_nodes


class Engine:
    def __init__(self, package_name: str, format: str):
        """Constructor method.

        Args:
            package_name: name of the package to visualise.
        """
        try:
            self.module = import_module(package_name)
        except ModuleNotFoundError:
            raise ValueError(f"invalid package_name. No module named `{package_name}`")

        self.nodes: set[Node] = set()
        self.graph = graphviz.Digraph(
            "pkgviz",
            format=format,
            node_attr={"color": "lightblue2", "style": "filled"},
            graph_attr={"overlap": "scale"},
            engine="neato",
        )

    def construct(self):
        """Constructs a set of nodes from input module."""
        self.nodes = construct_nodes(self.module)

    def draw(self):
        """Draws a DOT graph using constructed set of nodes."""
        for node in self.nodes:
            if node.children:
                for child in node.children:
                    self.graph.edge(node.name, child.name)

    def save(self, output_path: str):
        """Renders DOT graph and saves to output path.

        Args:
            output_path: path to save rendered visualisation.
        """
        self.graph.render(
            Path(output_path).name, Path(output_path).parent, cleanup=True
        )
