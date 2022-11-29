"""Define the main controller."""
import random
from typing import List
from models.player import Player
from models.game import Game
from models.round import Round
from models.tournament import Tournament

NUMBERS_PLAYERS = 8

class Controller:
    """Main controller."""

    def __init__(self, tournament: Tournament, view=""):
        """Has a Tournament, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.tournament = tournament

        # views
        self.view = view

    def get_players(self):
        """Get some players."""
        while len(self.players) < NUMBERS_PLAYERS:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def sort_players_rank(self):
        """Sort the players by their ranks."""
        return sorted(self.players, key=lambda player: player.rank)

    def sort_players_score(self):
        """Sort the players by their scores."""
        return sorted(self.players, key=lambda player: player.score, reverse=True)

    def generate_pairs_first_round(self):
        """Create pairs for the first round (swiss rules)."""
        pairs_first_round = []
        self.players = self.sort_players_rank()
        half = len(self.players) // 2
        upper_list = self.players[:half]
        lower_list = self.players[half:]
        for i, j in zip(range(len(upper_list)), range(len(lower_list))):
            pairs_first_round.append((upper_list[i], lower_list[j]))
        return pairs_first_round

    def update_tournament_players(self):
        for game in self.tournament.tournament_rounds.games:
            self.players.pop(self.view.choose_game_winner())

    def generate_pairs_next_round(self):
        """Create pairs for the others rounds (swiss rules)."""
        pairs_next_rounds = []
        list_scores = [player.score for player in self.players]
        for score in list_scores:
            if list_scores.count(score) > 1:
                self.players = self.sort_players_rank()
            else:
                self.players = self.sort_players_score()
        for i in range(len(self.players)-1):
            if (self.players.index(self.players[i]) % 2) == 0:
                pairs_next_rounds.append((self.players[i], self.players[i+1]))
        return pairs_next_rounds

    def update_scores(self):
        """Update the players scores after each round."""
        new_score = self.view.enter_scores()
        for player in self.players:
            player.score += new_score
        return self.players

    def generate_pairs_swiss_rules(self):
        running = True
        while running:
            self.generate_pairs_first_round()
            self.update_tournament_players()
            self.generate_pairs_next_round()













