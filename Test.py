from models.game import Game
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from tinydb import TinyDB
import json


sofiane = Player("Sofiane", "M.L")
anas = Player("Anas", "Aamoum")
kasparov = Player("Garry", "Kasparov")
fischer = Player("Bobby", "Fischer")
nakamura = Player("Hikaru", "Nakamura")
game1 = [Game(sofiane, kasparov)]
game2 = [Game(anas, fischer)]
games = [game1, game2]
t1 = Tournament("Championnat du monde d'echecs",
                 "Paris",
                 "16/11/2022",
                 "23/11/2022",
                 "time_control",
                 "description",
                 2
                )


r1 = Round("Round initial", "8:00 a.m", "11:00 a.m", 1)
r2 = Round("1/8 de final", "1:00 p.m", "03:00 p.m", 2)
t1.add_rounds([r1, r2])
t1.add_players([sofiane, anas, kasparov, fischer])
r1.add_games(game1)
r1.add_games(game2)
r2.add_games(game1)

Player.serialize_players()
Tournament.save_tournaments()

#Tournament.deserialize_tournament()






