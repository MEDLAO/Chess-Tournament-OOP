from models.player import Player


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
