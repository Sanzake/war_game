import random

numbers = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
suite = "HCDS"


def create_card(rank: str, suite: str) -> dict:
    return {"rank": rank, "suite": suite, "value": numbers[rank]}


def compare_cards(p1_card: dict, p2_card: dict):
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    if p1_card["value"] < p2_card["value"]:
        return "p2"
    else:
        return "WAR"


def create_deck() -> list[dict]:
    deck = []
    for s in suite:
        for n in numbers:
            deck.append(create_card(n, s))
    return deck


def shuffle(deck: list[dict]) -> list[dict]:
    counter = 0
    while counter < 1000:
        x1 = random.randint(0, 51)
        x2 = random.randint(0, 51)
        if x1 == x2:
            continue
        deck[x1], deck[x2] = deck[x2], deck[x1]
        counter += 1
    return deck
