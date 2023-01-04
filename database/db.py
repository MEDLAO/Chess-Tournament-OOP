from tinydb import TinyDB

db = TinyDB("database/db.json", indent=4)

players_table = db.table("Players")
tournament_table = db.table("Tournament")
