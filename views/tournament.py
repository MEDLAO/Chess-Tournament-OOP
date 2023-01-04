from models.player import Player
from models.tournament import Tournament, GameType
from controllers.tournament import create_first_round
from views.round import show_round_menu, show_all_games
from views.table import myTable, myTournamentTable


class TournamentView:
    @staticmethod
    def print_all():
        tournament_list = Tournament.get_all_tournaments()

        print("List of all tournaments:")
        myTable.clear_rows()
        for i, t in enumerate(tournament_list):
            myTable.add_row([
                i+1,
                t.tournament_name,
                t.tournament_place,
                t.time_control,
                t.description
            ])
        print(myTable)

    @staticmethod
    def add_tournament():
        print("Input Tournament info:")
        print("0 - Cancel")
        fields = ["tournament_name",
                  "tournament_place",
                  "description",
                  "number_rounds"
                  ]
        values = {}
        print("")
        print("Choose an option for the time_control: ")
        for elt in GameType:
            print(elt.value, "_", elt.name)
        option = int(input())
        for elt in GameType:
            if option == elt.value:
                values["time_control"] = elt.name

        for key in fields:
            value = input(f"Enter {key.replace('_', ' ')}: ")
            if key == "number_rounds":
                value = int(value)

            if value == "0":
                print("Adding tournament Cancelled! Returning to main menu...")
                return

            values[key] = value

        print("Choose players to add to the tournament")
        all_ps = Player.get_all_players()
        if len(all_ps) == 0:
            print("No players in the database")
        else:
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
        create_first_round(trn)
        Tournament.save_tournaments()
        print("Tournament Added to the database!")

    @classmethod
    def access_tournament(cls):
        while True:
            Tournament.save_tournaments()
            print("Choose the tournament you want to access:")
            all_ts = Tournament.get_all_tournaments()
            cls.print_all()

            choice = input("Choose number of tournament (0 to cancel): ")
            if choice == "0":
                print("returning to main menu...")
                break
            else:
                choice = int(choice) - 1
                chosen_tournament = all_ts[choice]
                show_all_games(chosen_tournament)
                trn = chosen_tournament
                show_round_menu(trn)


class TournamentMenu:
    @staticmethod
    def show_tournaments_menu():
        print("\n")
        print("######################")
        print("Show Tournaments Menu")
        print("######################")
        print("Tournaments:")
        Tournament.save_tournaments()
        while True:
            tournaments_list = Tournament.get_all_tournaments()
            if len(tournaments_list) == 0:
                print("\n")
                print("//No tournament in the database//")
            else:
                myTournamentTable.clear_rows()
                for i, t in enumerate(tournaments_list):
                    if t.tournament_start_date != "" and t.tournament_end_date == "":
                        myTournamentTable.add_row(["", f"{i+1}:{t}"])
                    else:
                        myTournamentTable.add_row([f"{i + 1}:{t}", ""])
                print(myTournamentTable)
            print("")
            print("What do you want to do?")
            print("1- Add a tournament")
            print("2- Access tournament")
            print("0- Return to previous menu ")
            choice = input("Choose option: ")
            if choice == "0":
                print("Aborted. Returning to previous menu")
                break
            elif choice == "1":
                TournamentView.add_tournament()
            elif choice == "2":
                TournamentView.access_tournament()
            else:
                print("Wrong choice. Try again")
