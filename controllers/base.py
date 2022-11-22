"""Define the main controller."""

from models.player import Player
from models.round import Round
from models.tournament import Tournament

NUMBERS_PLAYERS = 8

class Controller:
    """Main controller."""

    def __init__(self, tournament: Tournament, view):
        """Has a Tournament, a list of players and a view."""
        # models
        self.all_players: List[Player] = []
        self.tournament = tournament

        # views
        self.view = view

    def get_players(self):
        """Get some players."""
        while len(self.all_players) < NUMBERS_PLAYERS:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.all_players.append(player)