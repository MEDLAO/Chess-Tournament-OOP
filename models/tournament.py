from copy import deepcopy
from enum import Enum
from typing import List
from database.db import tournament_table
from models.player import Player
from models.round import Round


class GameType(Enum):
    BLITZ = 1
    BULLET = 2
    COUP_RAPIDE = 3


class Tournament:
    """Setup of a tournament."""
    _tournaments_list = []
    _id = 0

    def __init__(self,
                 tournament_name,
                 tournament_place,
                 time_control,
                 description,
                 number_rounds=4,
                 tournament_start_date="",
                 tournament_end_date="",
                 tournament_players=[],
                 tournament_participants={},
                 tournament_rounds=[]
                 ):
        Tournament._id += 1
        self.tournament_id = Tournament._id
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.time_control = time_control
        self.description = description
        self.number_rounds = number_rounds
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.tournament_players = tournament_players
        self.tournament_participants = tournament_participants
        self.tournament_rounds = tournament_rounds

        Tournament._tournaments_list.append(self)
        Tournament.serialize_tournament(self)

    def __str__(self):
        """Used in print."""
        return f"Tournament : {self.tournament_name}"

    def __repr__(self):
        return str(self)

    @classmethod
    def get_all_tournaments(cls):
        return cls._tournaments_list

    def add_players(self, tournament_players: List[Player]):
        """ Add a list of Player objects to the tournament."""
        self.tournament_players.extend(tournament_players)
        for player in tournament_players:
            self.tournament_participants[player.number] = 0

    def add_rounds(self, tournament_rounds: List[Round]):
        """Add a list of Round objects to the tournament."""
        self.tournament_rounds.extend(tournament_rounds)

    def serialize_tournament(self):
        """Prepare the dictionary for the serialization."""
        dict_tournament = deepcopy(vars(self))
        dict_tournament["tournament_players"] = [p.number for p in dict_tournament["tournament_players"]]
        dict_tournament["tournament_rounds"] = [r.serialize_round() for r in dict_tournament["tournament_rounds"]]
        return dict_tournament

    @classmethod
    def save_tournaments(cls):
        """Save the tournament in the database."""
        all_tournaments_dicts = []
        for tournament in cls._tournaments_list:
            dict_tournament = tournament.serialize_tournament()
            all_tournaments_dicts.append(dict_tournament)

        tournament_table.truncate()
        tournament_table.insert_multiple(all_tournaments_dicts)

    @classmethod
    def deserialize_tournaments(cls):
        """Extract a list of tournament from the database and transform it into Tournament objects. """
        deserialized_tournaments = tournament_table.all()

        for tournament_dict in deserialized_tournaments:
            tournament_dict["tournament_players"] = [
                Player.get_player_by_id(p_s) for p_s in tournament_dict["tournament_players"]
            ]
            tournament_dict["tournament_rounds"] = [
                Round.deserialize_round(r) for r in tournament_dict["tournament_rounds"]
            ]
            del tournament_dict["tournament_id"]
            cls(**tournament_dict)

        return cls._tournaments_list
