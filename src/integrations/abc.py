from .const import *

NAME = "name"
INGREDIENTS = "ingredients"
WORK = "work"

__pot_db = {
    HEALING: {
        NAME: "Mending Brew",
        INGREDIENTS: {NETTLE: 2, NEWT: 1, EGG: 1},
        WORK: 2
    },
    SLEEP: {
        NAME: "Morpheus' Kingdom",
        INGREDIENTS: {ELEMENTIUM: 1, LEMON: 2, FLOUR: 1},
        WORK: 5
    },
    FIRE: {
        NAME: "Flash Powder",
        INGREDIENTS: {RADISH: 5, LOTUS: 1},
        WORK: 3
    },
    NOCTURNAL: {
        NAME: "Bat Eye Potion",
        INGREDIENTS: {CARP: 1, MUSHROOMS: 3, LOTUS: 1, TOAD: 1},
        WORK: 12
    },
    STRENGTH: {
        NAME: "Flex Salve",
        INGREDIENTS: {FLOUR: 3, NEWT: 2},
        WORK: 5
    },
    MEMORY: {
        NAME: "Big Brain Solution",
        INGREDIENTS: {LOTUS: 2, NEWT: 10},
        WORK: 15
    },
    PRAYER: {
        NAME: "Liquid Faith",
        INGREDIENTS: {NETTLE: 10, ELEMENTIUM: 2},
        WORK: 42
    }
}


def lookup_potion(pot_id: str) -> dict:
    """
    Returns information about a given potion by its ID.
    :param pot_id:
    :return:
    """
    if pot_id in __pot_db:
        return __pot_db[pot_id]
    else:
        raise FileNotFoundError(f"404: No potion with id='{pot_id}' is found in the database.")


def lookup_ingredient(ing_id: str) -> dict:
    """
    Returns information about a given ingredient by its ID
    :param ing_id:
    :return:
    """
    pass
