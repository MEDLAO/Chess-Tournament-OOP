from typing import List
from models.game import Game


class Round:
    """Round."""

    def __init__(self, round_name="", start_date_time="", end_date_time="", number=""):
        """Has a name, start/end date and time."""
        self.round_name = round_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.number = number
        self.games = []

    def __str__(self):
        """Used in print."""
        return f"Round : {self.round_name}"

    def __repr__(self):
        return str(self)

    def add_games(self, games: List[Game]):
        self.games.extend(games)

    def serialize_round(self):
        dict_round = vars(self)
        dict_round["games"] = [g.serialize_game() for g in dict_round["games"]]
        return dict_round

    @classmethod
    def deserialize_round(cls, deserialized_round):
        rnd = Round(
            deserialized_round["round_name"],
            deserialized_round["start_date_time"],
            deserialized_round["end_date_time"],
            deserialized_round["number"]
        )
        rnd.games = [Game.deserialize_game(game) for game in deserialized_round["games"]]
        return rnd
