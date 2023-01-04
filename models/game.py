from models.player import Player


class Game:
    """Game."""

    def __init__(self, player_1: Player, player_2: Player, winner_game=None):
        """A list correspond to a player. Each list has two elements name and score."""
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner_game = winner_game

    def __str__(self):
        """Used in print."""
        return f"{self.player_1} vs {self.player_2} | Winner : {self.winner_game}"

    def __repr__(self):
        return str(self)

    def serialize_game(self):
        dict_game = {
            "player_1": self.player_1.number,
            "player_2": self.player_2.number,
        }
        if self.winner_game:
            dict_game["winner_game"] = self.winner_game
        return dict_game

    @classmethod
    def deserialize_game(cls, deserialized_game):
        deserialized_game["player_1"] = Player.get_player_by_id(deserialized_game["player_1"])
        deserialized_game["player_2"] = Player.get_player_by_id(deserialized_game["player_2"])
        game = cls(**deserialized_game)
        return game
