"""Base view."""

class View:
    """Swiss tournament view."""
    def main_menu(self):
        print("1-Commencer un tournoi/2-Terminer le round/3-Prochain round/4-Arrêter le tournoi")
        option = int(input("Choisir une option : "))
        return option

    def prompt_for_player(self):
        """Prompt for a name."""
        print("Tapez les informations du joueur:")
        first_name = input("Prénom : ")
        last_name = input("Nom de famille : ")
        score = input("Score : ")
        date_of_birth = input("Date de naissance-jj/mm/aaaa : ")
        sex = input("Sexe-M/F : ")
        rank = input("Rang : ")
        if not (first_name and last_name and score and date_of_birth and sex and rank):
            return None
        elif not (first_name or last_name or score or date_of_birth or sex or rank):
            print("Le profil du joueur n'est pas complet.")
        else:
            return first_name, last_name, score, date_of_birth, sex, rank

    def tournament_info(self):
        """"""
        print("Tapez les informations du tournoi :")
        tournament_name = input("Nom du tournoi : ")
        tournament_place = input("Lieu du tournoi : ")
        description = input("Description du tournoi : ")
        if not (tournament_name and tournament_place and description):
            return None
        elif not (tournament_name or tournament_place or description):
            print("Information(s) manquante(s).")
        else :
            return tournament_name, tournament_place, description

    def round_info(self):
        """"""
        print("Tapez le nom du tour :")
        round_name = input("Nom du tour : ")
        if not round_name:
            return None
        return round_name

    def winner_game_is(self, game):
        print(f"Indiquez le gagnant de la partie : {game}.")
        winner = int(input(f"1-{game.player_1.number}/2-{game.player_2.number}: "))
        return winner

    def show_game(self, game):
        print(game)

    def show_winner_tournament(self, player):
        """Show and congratulate the winner of the tournament."""
        print(f"Bravo {player.first_name} {player.last_name} !")










