from models.player import Player
from models.tournament import Tournament
from controllers.tournament import create_rounds


class TournamentView:
    @staticmethod
    def print_all():
        tournament_list = Tournament.get_all_tournaments()

        print("List of all tournaments:")
        for t in tournament_list:
            print(f"- {t}")

    @staticmethod
    def add_tournament():
        print("Input Tournament info:")
        print("0 - Cancel")
        fields = ["tournament_name", "tournament_place", "description"]
        values = {}
        for key in fields:
            value = input(f"Enter {key.replace('_', ' ')}: ")
            if value == "0":
                print("Adding tournament Cancelled! Returning to main menu...")
                return

            values[key] = value

        print("Choose players to add to the tournament")
        all_ps = Player.get_all_players()
        for i, p in enumerate(all_ps):
            print(f"{i + 1} - {p}")

        choice = input("Write the numbers of the players to add to the tournament. Separate by a space: ")
        choices = choice.split()
        try:
            chosen_players = []
            for number in choices:
                chosen_players.append(all_ps[int(number) - 1])

            chosen_players = list(set(chosen_players))
            if len(chosen_players) % 2 != 0 or len(chosen_players) < 2:
                print("The number of added players must be pair and > 2")
                return

        except:
            print("Bad choices of players. Aborted")
            return

        # Add validators
        trn = Tournament(**values)
        trn.add_players(chosen_players)
        create_rounds(trn)
        Tournament.save_tournaments()
        print("Tournament Added to the database!")


    @staticmethod
    def access_tournament():
        while True:
            print("Choose the tournmanent you want to access:")
            all_ts = Tournament.get_all_tournaments()
            for i, t in enumerate(all_ts):
                print(f"{i + 1} : id:{t.tournament_id} - {t.tournament_name}")

            choice = input("Choose number of tournament (0 to cancel): ")
            if choice == "0":
                print("returning to main menu...")
                return

            try:
                choice = int(choice) - 1
                chosen_tournament = all_ts[choice]

                TournamentMenu.show_menu(chosen_tournament)
            except:
                print("Bad choice. Try again please!\n")


class TournamentMenu:
    @staticmethod
    def show_menu(trn: Tournament):
        print("\n")
        print("###########")
        print("Tournament Menu")
        print("###########")
        print("Name:", trn.tournament_name)
        print("players:")
        for p in trn.tournament_players:
            print(Player.get_player_by_id(p))
        while True:
            print("What do you want to do?")
            print("1 - Show rounds list")
            print("2- Access round")
            print("0- Return to previous menu ")
            choice = input("Choose option: ")
            if choice == "0":
                print("Aborted. Returning to previous menu")
                break
            elif choice == "1":
                print(trn.tournament_rounds)
            elif choice == "2":
                # Menu to access roud TBD
                pass
            else:
                print("Wrong choice. Try again")

