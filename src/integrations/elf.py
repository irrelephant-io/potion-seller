from .db import make_inventory as _make


def read_inventory():
    """
    Returns the list of available inventory items in the form of a list of dictionaries
    """

    return _make()
