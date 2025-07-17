# db_utils.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
mongoURI = f"mongodb+srv://{username}:{password}@cluster0.xgo30b6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(mongoURI)
db = client["pydb"]
collection = db["data"]

# 🔁 CREATE
def insert_data(data):
    result= collection.insert_one(data)
    return result.inserted_id

# 🔎 READ
def get_all_data():
    return list(collection.find())

# ✏️ UPDATE
def update_data(query, new_values):
    return collection.update_one(query, {'$set': new_values})

# ❌ DELETE
def delete_data(query):
    return collection.delete_one(query)
