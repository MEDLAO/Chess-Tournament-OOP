from models.game import Game


def winner_game_is(game: Game, list_participant):
    """We choose the winner of the game then the score is set automatically."""

    print(f"Choose the winner for the game : {game}.")
    winner = int(input(f"1-{game.player_1}|2-{game.player_2}|3-DRAW : "))
    if winner == 1:
        game.winner_game = game.player_1.number
        list_participant[game.player_1.number] += 1
    elif winner == 2:
        game.winner_game = game.player_2.number
        list_participant[game.player_2.number] += 1
    elif winner == 3:
        game.winner_game = "DRAW"
        list_participant[game.player_1.number] += 0.5
        list_participant[game.player_2.number] += 0.5
    else:
        print("Please choose 1, 2 or 3.")
