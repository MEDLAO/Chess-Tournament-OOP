from typing import List
from tinydb import TinyDB
import json
from models.player import Player
from models.round import Round


# This is the file where our database will be saved
db = TinyDB("db.json", indent=4)

class Tournament:
    """Setup of a tournament."""

    rounds_list = []

    def __init__(self,
                 tournament_name,
                 tournament_place,
                 tournament_start_date,
                 tournament_end_date,
                 time_control,
                 description,
                 number_round=4,
                 ):
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.time_control = time_control
        self.description = description
        self.number_round = number_round
        self.players = []
        self.rounds = []

    def __str__(self):
        """Used in print."""
        return f"Tournament : {self.tournament_name}"

    def add_players(self, players: List[Player]):
        """
        Add a list of Player objects to the tournament
        Args:
            players:

        Returns:

        """
        self.players.extend(players)

    def add_rounds(self, rounds: List[Round]):
        self.rounds.extend(rounds)

    def serialize_tournament(self):
        """
        Prepare the dictionary for the serialization
        Returns:
        """
        db = TinyDB("db.json", indent=4)

        players_table = db.table("Players")
        players_table.truncate()
        for p in self.players:
            if p.serialize_player() not in players_table:
                players_table.insert(p.serialize_player())


        dict_tournament = vars(self)
        dict_tournament["players"] = [p.__str__() for p in self.players]
        dict_tournament["rounds"] = [r.serialize_round() for r in self.rounds]
        tournament_table = db.table("Tournament")
        tournament_table.truncate()
        tournament_table.insert(dict_tournament)
        return dict_tournament

    def deserialize_tournament(dict_tournament):
        tournament_name = dict_tournament['tournament_name']
        tournament_place = dict_tournament['tournament_place']
        tournament_start_date = dict_tournament['tournament_start_date']
        tournament_end_date = dict_tournament['tournament_end_date']
        time_control = dict_tournament['time_control']
        description = dict_tournament['description']
        number_round = dict_tournament['number_round']

        return Tournament(tournament_name=tournament_name,
                          tournament_place=tournament_place,
                          tournament_start_date=tournament_start_date,
                          tournament_end_date=tournament_end_date,
                          time_control=time_control,
                          description=description,
                          number_round=number_round
                         )
































