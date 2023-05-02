from random import shuffle, seed

TYPE = "type"
POTION = "p"
INGREDIENT = "i"
ID = "id"


def __make_pot(pot_id: str) -> dict[str, str]:
    return {TYPE: POTION, ID: pot_id}


def __make_inventory():
    yield from [__make_pot("83a5dbce") for _ in range(13)]
    yield from [__make_pot("3007b992") for _ in range(3)]
    yield from [__make_pot("a94b1729") for _ in range(3)]


def read_inventory():
    """
    Returns the list of available inventory items in the form of a list of dictionaries
    """
    seed("read_inventory")
    inventory = list(__make_inventory())
    shuffle(inventory)
    return inventory
