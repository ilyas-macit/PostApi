from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import os


class Database:
    def __init__(self, uri: str, db_name: str, collection: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    def get_all(self, filter=None):
        return self.collection.find(filter)

    def get(self, filter):
        return self.collection.find_one(filter)

    def add(self, item):
        self.collection.insert_one(item)

    def delete(self, id):
        self.collection.find_one_and_delete({"_id": ObjectId(id)})

    def update(self, id, item):
        self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": dict(item)})
