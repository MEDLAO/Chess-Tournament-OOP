from typing import List

from tinydb import TinyDB
import json

from models.player import Player
from models.round import Round
from models.tournament import Tournament

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


