from datetime import datetime

from models.game import Game
from models.round import Round
from models.tournament import Tournament


def generate_pairs_first_round(rnd, trn_players):
    """Create pairs for the first round (swiss rules)."""
    players = sorted(trn_players, key=lambda x: x.rank)
    half = len(players) // 2
    upper_list = players[:half]
    lower_list = players[half:]
    for i, j in zip(range(len(upper_list)), range(len(lower_list))):
        rnd.games.append(Game(upper_list[i], lower_list[j]))


def create_rounds(trn: Tournament):
    for i in range(trn.number_rounds):
        trn.tournament_rounds.append(Round(f"R{i + 1}"))

    first_round = trn.tournament_rounds[0]
    first_round.start_date_time = str(datetime.now())

    generate_pairs_first_round(first_round, trn.tournament_players)


