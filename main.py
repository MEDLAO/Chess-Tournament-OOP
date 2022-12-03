from models.player import Player
from models.tournament import Tournament
from views.player import PlayerView
from views.tournament import TournamentView


# 1st step: Load data from the database.

Player.deserialize_players()  # Load players from the database
Tournament.deserialize_tournaments()  # Load players from the database


print("#############################")
print("### Welcome to chess soft ###")
print("#############################")
print("Load Complete!")
while True:
    print("\n")
    print("What do you want to do?")
    print("1 - Show players")
    print("2 - Add a player")
    print("3 - Show tournaments")
    print("4 - Add a tournament")
    print("5 - Access tournament")
    print("0 - Close program")
    choice = input("Choose an option: ")
    if choice == "1":
        # The view to show all players
        PlayerView.print_all()
    elif choice == "2":
        # The view to add a player
        PlayerView.add_player()
    elif choice == "3":
        # The view to show all tournaments
        TournamentView.print_all()
    elif choice == "4":
        # The view to add a tournament
        TournamentView.add_tournament()
    elif choice == "5":
        TournamentView.access_tournament()

    elif choice == "0":
        print("Good Bye")
        break
    else:
        print("Wrong choice. Please choose a correct option")


