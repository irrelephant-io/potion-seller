from .ids import *
from random import shuffle, seed, sample
from uuid import uuid4

_NAME = "name"
_INGREDIENTS = "ingredients"
_WORK = "work"
_COST = "cost"
_SIDE_EFFECTS = "sideEffects"
_ALLERGENS = "allergens"
_TYPE = "type"
_POTION = "p"
_INGREDIENT = "i"
_ID = "id"

pot_db = {
    HEALING: {
        _NAME: "Mending Brew",
        _INGREDIENTS: {NETTLE: 2, NEWT: 1, EGG: 1},
        _WORK: 2
    },
    SLEEP: {
        _NAME: "Morpheus' Kingdom",
        _INGREDIENTS: {ELEMENTIUM: 1, LEMON: 2, FLOUR: 1},
        _WORK: 5
    },
    FIRE: {
        _NAME: "Flash Powder",
        _INGREDIENTS: {EGGPLANT: 5, LOTUS: 1},
        _WORK: 3
    },
    NOCTURNAL: {
        _NAME: "Bat Eye Potion",
        _INGREDIENTS: {CARP: 1, MUSHROOMS: 3, LOTUS: 1, TOAD: 1},
        _WORK: 12
    },
    STRENGTH: {
        _NAME: "Flex Salve",
        _INGREDIENTS: {FLOUR: 3, NEWT: 2},
        _WORK: 5
    },
    MEMORY: {
        _NAME: "Big Brain Solution",
        _INGREDIENTS: {LOTUS: 2, NEWT: 10},
        _WORK: 15
    },
    PRAYER: {
        _NAME: "Liquid Faith",
        _INGREDIENTS: {NETTLE: 10, ELEMENTIUM: 2},
        _WORK: 42
    }
}

ingredient_db = {
    NETTLE: {
        _NAME: "Common Nettle",
        _COST: 2,
        _SIDE_EFFECTS: {"Heartburn"},
        _ALLERGENS: {}
    },
    FLOUR: {
        _NAME: "Stone-ground Wheat Flour",
        _COST: 2,
        _SIDE_EFFECTS: {},
        _ALLERGENS: {"Gluten"}
    },
    LOTUS: {
        _NAME: "Pink Lotus Petals",
        _COST: 10,
        _SIDE_EFFECTS: {"Insomnia"},
        _ALLERGENS: {"Pollen"}
    },
    NEWT: {
        _NAME: "Eye of Newt",
        _COST: 5,
        _SIDE_EFFECTS: {"Googly Eyes", "Vomiting"},
        _ALLERGENS: {}
    },
    ELEMENTIUM: {
        _NAME: "Elementium Powder",
        _COST: 15,
        _SIDE_EFFECTS: {"Skepticism", "Vomiting", "Death"},
        _ALLERGENS: {}
    },
    EGGPLANT: {
        _NAME: "Eggplant",
        _COST: 4,
        _SIDE_EFFECTS: {"Vomiting"},
        _ALLERGENS: {"Nightshade"}
    },
    MUSHROOMS: {
        _NAME: "Toadstool",
        _COST: 2,
        _SIDE_EFFECTS: {"Diarrhea", "Vomiting", "Hallucinations", "Death"},
        _ALLERGENS: {"Spores"}
    },
    LEMON: {
        _NAME: "Lemon Zest",
        _COST: 7,
        _SIDE_EFFECTS: {},
        _ALLERGENS: {"Citrus"}
    },
    EGG: {
        _NAME: "Egg Yolk",
        _COST: 2,
        _SIDE_EFFECTS: {},
        _ALLERGENS: {"Egg"}
    },
    TOAD: {
        _NAME: "Toad Tongue",
        _COST: 8,
        _SIDE_EFFECTS: {"Heartburn"},
        _ALLERGENS: {}
    },
    CARP: {
        _NAME: "Carp Row",
        _COST: 10,
        _SIDE_EFFECTS: {},
        _ALLERGENS: {"Fish"}
    }
}


def __make_of_type(item_id: str, item_type: str) -> dict[str, str]:
    return {_ID: item_id, _TYPE: item_type}


def __make_pot(pot_id: str) -> dict[str, str]:
    return __make_of_type(pot_id, _POTION)


def __make_ingredient(ingredient_id: str) -> dict[str, str]:
    return __make_of_type(ingredient_id, _INGREDIENT)


def __make_random_id():
    return str(uuid4()).split('-')[0]

def __make_inventory():
    # Make potions
    yield from [__make_pot(HEALING) for _ in range(13)]
    yield from [__make_pot(SLEEP) for _ in range(3)]
    yield from [__make_pot(FIRE) for _ in range(3)]
    yield from [__make_pot(NOCTURNAL) for _ in range(5)]
    yield from [__make_pot(STRENGTH) for _ in range(2)]
    yield from [__make_pot(PRAYER) for _ in range(2)]

    # Make ingredients
    yield from [__make_ingredient(NETTLE) for _ in range(5)]
    yield from [__make_ingredient(FLOUR) for _ in range(20)]
    yield from [__make_ingredient(LOTUS) for _ in range(3)]
    yield from [__make_ingredient(NEWT) for _ in range(7)]
    yield from [__make_ingredient(ELEMENTIUM) for _ in range(1)]
    yield from [__make_ingredient(EGGPLANT) for _ in range(4)]
    yield from [__make_ingredient(MUSHROOMS) for _ in range(10)]
    yield from [__make_ingredient(LEMON) for _ in range(1)]
    yield from [__make_ingredient(TOAD) for _ in range(3)]
    yield from [__make_ingredient(CARP) for _ in range(10)]

    junk_types = ['x', 'f', 'a', 'k']
    # Make junk
    yield from [
        __make_of_type(__make_random_id(), sample(junk_types, 1)[0])
        for _ in range(5)
    ]


def make_inventory():
    seed("read_inventory")
    inventory = list(__make_inventory())
    shuffle(inventory)
    return inventory
