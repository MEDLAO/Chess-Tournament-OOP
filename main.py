from models.player import Player
from models.tournament import Tournament
from views.player import PlayerView
from views.tournament import TournamentMenu


# 1st step: Load data from the database.

Player.deserialize_players()  # Load players from the database
Tournament.deserialize_tournaments()  # Load tournaments from the database


print("#############################")
print("### Welcome to chess soft ###")
print("#############################")
print("Load Complete!")
while True:
    print("\n")
    print("What do you want to do?")
    print("1 - Show players")
    print("2 - Add a player")
    print("3 - Change players ranking")
    print("4 - Show tournaments")
    print("0 - Close program")
    choice = input("Choose an option: ")
    if choice == "1":
        # The view to show all players
        if Player._player_list == []:
            print("//No players in the database//")
        else:
            PlayerView.show_menu_players()
    elif choice == "2":
        # The view to add a player
        PlayerView.add_player()
    elif choice == "3":
        PlayerView.change_rank_players()
        Player.serialize_players()
    elif choice == "4":
        # The view to show all tournaments
        TournamentMenu.show_tournaments_menu()
    elif choice == "0":
        print("Good Bye")
        break
    else:
        print("Wrong choice. Please choose a correct option.")
