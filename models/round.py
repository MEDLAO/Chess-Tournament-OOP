from typing import List
from models.game import Game
from database.db import tournament_table

class Round:
    """Round."""

    def __init__(self, round_name, start_date_time, end_date_time, number):
        """Has a name, start/end date and time."""
        self.round_name = round_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.number = number
        self.games = []

    def __str__(self):
        """Used in print."""
        return f"Round : {self.round_name}"

    def add_games(self, games: List[Game]):
        self.games.extend(games)

    def serialize_round(self):
        #if True:
        #   return {}
        dict_round = vars(self)
        dict_round["games"] = [g.__str__() for g in dict_round["games"]]
        return dict_round

    def deserialize_round(deserialized_round):
        round = Round(
            deserialized_round["round_name"],
            deserialized_round["start_date_time"],
            deserialized_round["end_date_time"],
            deserialized_round["number"]
        )
        round.games = [Game.deserialize_game(game) for game in deserialized_round["games"]]
        return round






















