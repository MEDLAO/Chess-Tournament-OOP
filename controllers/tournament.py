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


def generate_pairs_next_rounds(rnd, trn_players, trn: Tournament):
    """Create pairs for the others rounds (swiss rules)."""
    result = trn.tournament_participants
    trn_players.sort(key=lambda player: player.rank, reverse=True)
    trn_players.sort(key=lambda player: result[player.number], reverse=True)

    all_tuples_games = []
    for r in trn.tournament_rounds:
        for game in r.games:
            all_tuples_games.append((game.player_1, game.player_2))

    tour_players = [p for p in trn_players]

    while len(tour_players) > 0:
        for p in tour_players:
            if tour_players[0] != p:
                if (tour_players[0], p) not in all_tuples_games and (p, tour_players[0]) not in all_tuples_games:
                    rnd.games.append(Game(tour_players[0], p))
                    tour_players.remove(tour_players[0])
                    tour_players.remove(p)
                    break
                else:
                    if p == tour_players[-1]:
                        rnd.games.append(Game(tour_players[0], p))
                        tour_players.remove(tour_players[0])
                        tour_players.remove(p)
    return rnd


# Other algorithm possible for the next rounds
"""i = 0 
    while i <= len(trn_players):
        combinations_tuples = [(tour_players[0], x) for x in tour_players[1:]]
        # get the first element that matches a condition
        # here the first tuple which is not in all_tuples_games
        for pair in combinations_tuples:
            if pair not in all_tuples_games and tuple(reversed(pair)) not in all_tuples_games:
                first = pair
                rnd.games.append(Game(first[0], first[1]))
                tour_players.remove(tour_players[0])
                tour_players.remove(first[1])
                break
            else:
                if pair == combinations_tuples[-1]:
                    last = combinations_tuples[-1]
                    rnd.games.append(Game(last[0], last[1]))
                    tour_players.remove(tour_players[0])
                    tour_players.remove(tour_players[-1])

        i += 1
    return rnd"""


def create_first_round(trn: Tournament):
    for i in range(trn.number_rounds):
        trn.tournament_rounds.append(Round(f"R{i + 1}"))

    first_round = trn.tournament_rounds[0]
    first_round.start_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    trn.tournament_start_date = first_round.start_date_time
    generate_pairs_first_round(first_round, trn.tournament_players)


def create_next_round(rnd, trn: Tournament):
    rnd.start_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    generate_pairs_next_rounds(rnd, trn.tournament_players, trn)
