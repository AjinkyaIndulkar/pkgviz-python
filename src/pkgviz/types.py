class Node:
    """Base data structure of the visualiser engine.

    A ``Node`` instance store a name for reference and a list of
    ``Node`` children to construct the final graph.
    """

    def __init__(self, name):
        """Constructor method.

        Args:
            name: name to identify node instance.
        """
        self.name = name
        self.children: list[Node] = []

    def __repr__(self):
        return f"Node(name={self.name}, children={[child.name for child in self.children]})"
