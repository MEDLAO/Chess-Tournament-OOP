import json
from pprint import pprint

from database.db import players_table


class Player:
    """Player."""

    _id = 0  # An id that we will increment each time we create a new player
    _player_list = []


    def __init__(self, first_name, last_name="", score=0, date_of_birth="", sex="M", rank=0):
        """Has a  first_name, a family_name,etc."""
        Player._id += 1
        self.number = f"P_{Player._id}"
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank
        # Add newly created Player to this list of all players
        Player._player_list.append(self)
        Player.serialize_players()

    def __str__(self):
        """Used in print."""
        return f"[{self.number}: {self.first_name} {self.last_name}, {self.rank}, {self.score}]"

    def __repr__(self):
        return str(self)

    @classmethod
    def get_all_players(cls):
        return cls._player_list

    @classmethod
    def get_player_by_id(cls, number):
        for player in cls._player_list:
            if player.number == number:
                return player

        raise ValueError("Player number not existing")

    @classmethod
    def serialize_players(cls):
        """
        Create a dictionary for Player, so it is ready at the serialization.
        """

        all_players_dicts = []
        for player in cls._player_list:
            dict_player = vars(player)
            all_players_dicts.append(dict_player)

        players_table.truncate()
        players_table.insert_multiple(all_players_dicts)

    @classmethod
    def deserialize_players(cls):
        all_players = players_table.all()
        for player in all_players:
            del player["number"]
            cls(**player)

    @classmethod
    def deserialize_player(deserialized_player):
        player = Player(
            deserialized_player["first_name"],
            deserialized_player["last_name"],
            deserialized_player["score"],
            deserialized_player["date_of_birth"],
            deserialized_player["sex"],
            deserialized_player["rank"]
        )
        return player






















