from models.player import Player
from models.round import Round
from models.tournament import Tournament
from controllers.base import Controller

sofiane = Player("Sofiane", "M.L", 50, rank=1)
anas = Player("Anas", "Aamoum", 50, rank=2)
kasparov = Player("Garry", "Kasparov", 45, rank=3)
carlsen = Player("Magnus", "Carlsen", 37, rank=4)
fischer = Player("Bobby", "Fischer", 35, rank=5)
nakamura = Player("Hikaru", "Nakamura", 35, rank=6)


gamers = [nakamura, sofiane, kasparov, anas, fischer, carlsen]
A = sorted(gamers, key=lambda x: x.rank)
B = sorted(gamers, key=lambda x: x.score, reverse= True)

#for elt in B:
#   print(elt)

t1 = Tournament("Championnat du monde d'echecs",
                 "Paris",
                 "16/11/2022",
                 "23/11/2022",
                 "time_control",
                 "description",
                 2
                )

r1 = Round("Round initial", "8:00 a.m", "11:00 a.m", 1)
controller = Controller(t1)
controller.players = gamers














"""for i in range(len(B)-1):
    if B.index(B[i]) < B.index(B[i+1]) and B[i].rank > B[i+1].rank:
        B[i], B[i+1] = B[i+1], B[i]"""

"""for x in B:
    print(x)"""







