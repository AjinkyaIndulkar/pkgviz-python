import pytest

from pkgviz.engine import Engine


def test_engine_exception():
    """Tests if Engine raises exception with incorrect input."""
    with pytest.raises(ValueError):
        Engine("dummy", "svg")
