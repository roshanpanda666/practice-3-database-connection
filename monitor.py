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

def on_new_data(data):
    print("New data inserted:")
    print(data)

with collection.watch([{"$match": {"operationType": "insert"}}]) as stream:
    for change in stream:
        new_data = change["fullDocument"]
        on_new_data(new_data)
