from war_game.utils.deck import create_deck, shuffle, compare_cards


def create_player(name: str = "AI") -> dict:
    player = {"name": name, "hand": [], "won_pile": []}
    return player


def init_game() -> dict:
    p1 = create_player("Dani")
    p2 = create_player()

    deck = create_deck()
    shuffle(deck)

    p1["hand"] = deck[:26]
    p2["hand"] = deck[26::]
    return {"deck": deck, "player_1": p1, "player_2": p2}


prize = []


def play_round(p1: dict, p2: dict):
    global prize
    if len(p1["hand"]) == 0 or len(p2["hand"]) == 0:
        return
    c1 = p1["hand"].pop(0)
    c2 = p2["hand"].pop(0)
    prize.append(c1)
    prize.append(c2)

    winner = compare_cards(c1, c2)

    if winner == "p1":
        p1["won_pile"].extend(prize)
        prize = []

    if winner == "p2":
        p2["won_pile"].extend(prize)
        prize = []

    if winner == "WAR":
        if len(p1["hand"]) >= 4:
            x = 3
        else:
            x = len(p1["hand"]) - 1
        for i in range(x):
            prize.append(p1["hand"].pop(0))

        if len(p2["hand"]) >= 4:
            x = 3
        else:
            x = len(p2["hand"]) - 1
        for i in range(x):
            prize.append(p2["hand"].pop(0))

        play_round(p1, p2)
