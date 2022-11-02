from pkgviz.types import Node


def test_node_repr():
    """Tests Node type's string representation."""
    node = Node("test")

    assert node.__repr__() == "Node(name=test, children=[])"

    node.children.append(Node("child_test"))

    assert node.__repr__() == "Node(name=test, children=['child_test'])"
