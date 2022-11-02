import inspect
import logging

from rich.logging import RichHandler

from .types import Node


def construct_nodes(module, name: str = None, nodes: set[Node] = None):
    """Construct all nodes of input module.

    Args:
        module: input module.
        name: name of module.
        nodes: set of all constructed nodes.
    """
    # if name is not passed, use name of input module
    if not name:
        name = module.__name__

    if not nodes:
        nodes = set()

    module_node, nodes = fetch_or_create_node(name, nodes)

    for member_name, member_module in inspect.getmembers(module):
        # check if child module needs to be ignored
        if (
            "__" in member_name
            or (
                inspect.ismodule(member_module)
                and name not in getattr(member_module, "__package__", "")
            )
            or (
                not inspect.ismodule(member_module)
                and name not in getattr(member_module, "__module__", "")
            )
        ):
            continue

        member_node, nodes = fetch_or_create_node(member_name, nodes)

        module_node.children.append(member_node)

        if inspect.ismodule(member_module):
            construct_nodes(member_module, member_name, nodes)

    return nodes


def fetch_or_create_node(name, nodes) -> tuple[Node, set[Node]]:
    """Fetch Node from set of constructed Nodes.

    If absent, create a new one.

    Args:
        name: name to fetch or create node.
        nodes: set of constructed nodes.

    Returns:
        tuple of fetched/constructed node and
        updated set of constructed nodes.
    """
    constructed_node = [n for n in nodes if n.name == name]

    if constructed_node:
        module_node = constructed_node[0]
    else:
        module_node = Node(name)
        nodes.add(module_node)

    return module_node, nodes


def get_logger(root_level: int = logging.INFO) -> logging.Logger:
    """Creates logger instance.

    Args:
        root_level: root level logging value.

    Returns:
        logger instance.
    """
    if logging.root.handlers == []:
        logging.basicConfig(
            level=root_level, handlers=[RichHandler(rich_tracebacks=True)]
        )

    logger = logging.getLogger("pkgviz")
    logger.setLevel(logging.root.level)

    return logger
