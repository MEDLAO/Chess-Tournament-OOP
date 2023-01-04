from models.player import Player
from models.tournament import Tournament


class PlayerView:
    @staticmethod
    def print_all():
        player_list = Player.get_all_players()

        print("List of all registered players:")
        for p in player_list:
            print(f"- {p}")

    @staticmethod
    def add_player():
        print("Input Player info:")
        print("0 - Cancel")
        fields = ["first_name", "last_name", "date_of_birth", "sex", "rank"]
        values = {}
        for key in fields:
            value = input(f"Enter {key.replace('_', ' ')}: ")
            if value == "0":
                print("Adding player Cancelled! Returning to main menu...")
                return

            values[key] = value

        # Add validators
        Player(**values)
        print("Player Added to the database!")

    @staticmethod
    def change_rank_players():
        player_list = Player.get_all_players()
        for p in player_list:
            print(p)
        choice = input("Write the numbers of the players you want to change the ranking : ")
        choices = choice.split()
        try:
            chosen_players = []
            for number in choices:
                chosen_players.append(Player.get_player_by_id(number))

        except ValueError:
            print("Bad choices of players. Aborted")
            return

        for p in chosen_players:
            new_ranking = int(input(f"Write the new ranking of {p} : "))
            p.rank = new_ranking

    @staticmethod
    def show_menu_players():
        while True:
            print("")
            print("1 - Show all players")
            print("2 - Show players of a tournament")
            choice = input("Choose an option (0 to cancel): ")
            if choice == "0":
                break
            elif choice == "1":
                while True:
                    print("")
                    print("1 - By alphabetical order ")
                    print("2 - By ranking")
                    option = input("Choose an option (0 to cancel): ")
                    if option == "0":
                        break
                    elif option == "1":
                        player_list = Player.get_all_players()
                        player_list.sort(key=lambda x: x.last_name)
                        for player in player_list:
                            print(player)
                    elif option == "2":
                        player_list = Player.get_all_players()
                        player_list.sort(key=lambda x: x.rank, reverse=True)
                        for player in player_list:
                            print(player)
                    else:
                        print("Wrong choice. Please choose a correct option.")
            elif choice == "2":
                while True:
                    print("\n")
                    Tournament.save_tournaments()
                    print("Choose the tournament you want to show the players:")
                    all_ts = Tournament.get_all_tournaments()
                    for i, t in enumerate(all_ts):
                        print(f"{i + 1} : {t.tournament_name}")

                    choice = input("Choose number of tournament (0 to cancel): ")
                    if choice == "0":
                        print("returning to main menu...")
                        break
                    else:
                        choice = int(choice) - 1
                        chosen_tournament = all_ts[choice]
                        while True:
                            print("")
                            print("1 - By alphabetical order ")
                            print("2 - By ranking")
                            option = input("Choose an option (0 to cancel) : ")
                            if option == "0":
                                break
                            elif option == "1":
                                chosen_tournament.tournament_players.sort(key=lambda x: x.last_name)
                                for player in chosen_tournament.tournament_players:
                                    print(player)
                            elif option == "2":
                                chosen_tournament.tournament_players.sort(key=lambda x: x.rank, reverse=True)
                                for player in chosen_tournament.tournament_players:
                                    print(player)
                            else:
                                print("Wrong choice. Please choose a correct option.")
            else:
                print("Wrong choice. Please choose a correct option.")
