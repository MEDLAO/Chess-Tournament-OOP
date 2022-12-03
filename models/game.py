from typing import List
from models.player import Player


class Game:
    """Game."""

    def __init__(self, player_1: Player, player_2: Player):
        """A list correspond to a player. Each list has two elements name and score."""
        self.player_1 = player_1
        self.player_2 = player_2

    def __str__(self):
        """Used in print."""
        return f"{self.player_1} vs {self.player_2}"

    def __repr__(self):
        return str(self)

    def deserialize_game(self):
        return self

























