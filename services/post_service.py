from dotenv import load_dotenv
from db.mongodb import Database
from bson import ObjectId
from models.post import Post, PostUpdateDto
from schemas.post_schemas import *
import os
load_dotenv("variables.env")

uri = os.getenv("MONGODB_CONNECTION_URI")
db_name = os.getenv("DATABASE_NAME")
collection = os.getenv("COLLECTION_NAME")
db = Database(uri, db_name, collection)


def get_all():
    posts = db.get_all()
    if posts is not None:
        return post_get_all_entities(posts)
    else:
        return Exception("Data could not be retrieved.")


def get_by_id(id):
    post = db.get({"_id": ObjectId(id)})
    if post is not None:
        return post_get_entity(post)
    else:
        return Exception("Post could not found")


def create_post( post):
    if post is not None:
        postData = post_create_entity(post)
        db.add(postData)
    else:
        return Exception("post cannot be None")


def update_post(id, post):
    if post is not None:
        postData = post_update_entity(post)
        db.update(id, postData)
    else:
        return Exception("Post cannot be None")


def delete_post(id):
    post = db.get({"_id": ObjectId(id)})
    if post is not None:
        db.delete(id)
    else:
        return Exception("Post cannot be None")
