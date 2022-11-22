from typing import List

from tinydb import TinyDB
import json

# This is the file where our database will be saved
db = TinyDB("db.json", indent=4)


class Model:
    """
    This is the mother class for our models Player and Tournament.
    These 2 models will be saved as tables in db.json
    """

    # This class variable will save all the models (in this project Tournament and Player)
    _objects = {}
    # Example
    # {
    #     "Player": ["liste des objects Player"],
    #     "Tournament": ["liste des objects Tournament"]
    # }

    def __init__(self, class_name):
        """
        Whenever a new object is created, it goes to the right list in the dictionary _objects
        Args:
            class_name: The name of the class where we save the new object (either Player or Tournament)
        """
        if class_name in Model._objects:
            Model._objects[class_name].append(self)
        else:
            Model._objects[class_name] = [self]

    @classmethod
    def serialize(cls):
        """
        Creates a table for the model in question
        Gets a json object from the list of objects of the model in question (Player or Tournament)
        Saves them in the right table
        Returns: None

        """
        table = db.table(cls.__name__)  # Table will have the name of the class that called this method
        table.truncate()

        # Prepare the json and write it in the table of the TinyDB file
        elements = [elm.prepare() for elm in cls._objects[cls.__name__]]
        json_str = json.dumps(elements)  # Gives a json format in string
        serialized_models = json.loads(json_str)  # To get an actual json object
        table.insert_multiple(serialized_models)  # insert_multiple accepts only json objects

    @classmethod
    def deserialize(cls):
        pass


class Player(Model):
    _id = 0  # An id that we will increment each time we create a new player

    def __init__(self, nom, age):
        Player._id += 1
        self.number = f"P_{Player._id}"
        self.nom = nom
        self.age = age
        super().__init__("Player")

    def prepare(self):
        """
        Create a dictionary for the model Player, so it is ready at the serialization.
        Returns:

        """
        return vars(self)


class Round:
    def __init__(self, number):
        self.number = number

    def prepare(self):
        return vars(self)


class Tournament(Model):
    def __init__(self, name):
        self.name = name
        self.players = []
        self.rounds = []
        super().__init__("Tournament")

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

    def prepare(self):
        """
        Prepare the dictionary for the serialization
        Returns:

        """
        res = vars(self)
        res["players"] = [p.number for p in self.players]
        res["rounds"] = [r.prepare() for r in self.rounds]
        return res









