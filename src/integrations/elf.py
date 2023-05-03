from .db import make_inventory as _make

_IS_READ = False


def read_inventory():
    """
    Returns the list of available inventory items in the form of a list of dictionaries
    """
    global _IS_READ

    if _IS_READ:
        raise SystemError("ELF needs time to recover from the previous read.")

    _IS_READ = True
    return _make()
