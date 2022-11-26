from models.player import Player
from models.tournament import Tournament

# Load players from the database
Player.deserialize_players()
print("My all players:")
for player in Player.get_all_players():
    print(player)
print("-------------------------")
all_ts = Tournament.deserialize_tournaments()
t1 = all_ts[0]
print(t1)
for player in t1.tournament_players:
    print(player)
print("-------------------------")
for round in t1.tournament_rounds:
    print("-------------------------")
    print(round)

    for game in round.games:
        print(game)


# print("Ajouter un joueur:")
# fn = input("First Name: ")
# ln = input("Last Name: ")
# Player(first_name=fn, last_name=ln)
#
# print("-------------------------")
# print("My all players:")
# for player in Player.get_all_players():
#     print(player)


