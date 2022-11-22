from typing import List
from models.game import Game


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
        dict_round = vars(self)
        dict_round["games"] = [r.__str__() for r in self.games]
        return dict_round

    def deserialize_round(dict_round):
        round_name = dict_round['round_name']
        start_date_time = dict_round['start_date_time']
        end_date_time = dict_round['end_date_time']
        number = dict_round['number']
        return Round(round_name=round_name,
                        start_date_time=start_date_time,
                        end_date_time=end_date_time,
                        number=number
                        )
















