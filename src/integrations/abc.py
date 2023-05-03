from .db import pot_db as _pot_db
from .db import ingredient_db as _ingredient_db


def lookup_potion(pot_id: str) -> dict:
    """
    Returns information about a given potion by its ID.
    :param pot_id:
    :return:
    """
    if pot_id in _pot_db:
        return _pot_db[pot_id]
    else:
        raise FileNotFoundError(f"404: No potion with id='{pot_id}' is found in the database.")


def lookup_ingredient(ing_id: str) -> dict:
    """
    Returns information about a given ingredient by its ID
    :param ing_id:
    :return:
    """
    if ing_id in _ingredient_db:
        return _ingredient_db[ing_id]
    else:
        raise FileNotFoundError(f"404: No ingredient with id='{ing_id}' is found in the database.")
