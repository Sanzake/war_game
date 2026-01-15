from war_game.game_logic.game import init_game, play_round


def main():
    game = init_game()
    while game["player_1"]["hand"] and game["player_2"]["hand"]:
        play_round(game["player_1"], game["player_2"])
    if len(game["player_1"]["won_pile"]) == len(game["player_2"]["won_pile"]):
        print("Dead heat")
    if len(game["player_1"]["won_pile"]) > len(game["player_2"]["won_pile"]):
        print("p1 is a winner")
    if len(game["player_1"]["won_pile"]) < len(game["player_2"]["won_pile"]):
        print("p2 is a winner")


if __name__ == "__main__":
    main()
