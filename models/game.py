from typing import List
from models.player import Player


class Game:
    """Game."""

    def __init__(self, player_1: Player, player_2: Player):
        """A list correspond to a player. Each list has two elements name and score."""
        self.player_1 = player_1
        self.player_2 = player_2

    def set_score(self, winner):
        if winner == 1:
            self.score_1 = 1
            self.score_2 = 0
        elif winner == 2:
            self.score_1 = 0
            self.score_2 = 1
        else:
            self.score_1 = 0.5
            self.score_2 = 0.5

    def __str__(self):
        """Used in print."""
        return f"{self.player_1} vs {self.player_2}"

    def __repr__(self):
        return str(self)


    def deserialize_game(self):
        return self

























