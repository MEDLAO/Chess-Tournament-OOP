from tinydb import TinyDB
import json


"""
    def deserialize(cls):
        pass

        f = open('db.json')
        data = json.load(f)

        for cle in data.keys():
            cls_keys_list = [key for key in data[cle]["1"].keys()]
            for elt in cls_keys_list:
                elt = data[cle]["1"][elt]
                return cls(elt)
        
        f.close()"""


class Player:
    """Player."""

    _id = 0  # An id that we will increment each time we create a new player

    def __init__(self, first_name, last_name, date_of_birth, sex, rank, score):
        """Has a  first_name, a family_name,etc."""
        Player._id += 1
        self.number = f"P_{Player._id}"
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank
        self.score = score

    def __str__(self):
        """Used in print."""
        return f"[{self.first_name} {self.last_name}, {self.score}]"

    def serialize_player(self):
        """
        Create a dictionary for Player, so it is ready at the serialization.
        """
        db = TinyDB("db.json", indent=4)
        dict_player = vars(self)
        players_table = db.table("Players")
        players_table.insert(dict_player)
        return dict_player

    def deserialize_player(dict_player):
        first_name = dict_player['first_name']
        last_name = dict_player['last_name']
        date_of_birth = dict_player['date_of_birth']
        sex = dict_player['sex']
        rank = dict_player['rank']
        score = dict_player['sex']
        return Player(first_name=first_name,
                        last_name=last_name,
                        date_of_birth=date_of_birth,
                        sex=sex,
                        rank=rank,
                        score=score
                        )


















