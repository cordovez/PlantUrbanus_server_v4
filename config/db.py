from dotenv import dotenv_values
from pymongo import MongoClient
env = dotenv_values(".env")

connection = MongoClient(env["MONGO_URI"])
db = env["MONGO_DB"]  # PlantUrbanus
mongo_db = connection[db]
