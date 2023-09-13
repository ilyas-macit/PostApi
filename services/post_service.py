from dotenv import load_dotenv
from db.mongodb import Database
from bson import ObjectId
from models.post import Post, PostUpdateDto
from schemas.post_schemas import *
import os
load_dotenv("../variables.env")
load_dotenv("variables.env")


uri = os.getenv("MONGODB_CONNECTION_URI")
db_name = os.getenv("DATABASE_NAME")
collection = os.getenv("COLLECTION_NAME")
db = Database(uri, db_name, collection)


def get_all():
    posts = db.get_all()
    if posts is None:
        raise Exception("Data could not be retrieved.")
    return post_get_all_entities(posts)


def get_by_id(id):
    post = db.get({"_id": ObjectId(id)})
    if post is None:
        raise Exception("Post could not found")
    return post_get_entity(post)


def create_post(post):
    #validation rules
    if post is None:
        raise ValueError("Post value cannot be None. You must specify a valid post.")
    if not isinstance(post, Post):
        raise TypeError("Input must be an instance of Post.")
    if not len(post.tags) > 0:
        raise Exception("Tags must be greater than 0")
    if not len(post.title) > 3:
        raise Exception("Title must be greater than 3 character")
    postData = post_create_entity(post)
    db.add(postData)
    return postData

def update_post(id, post):
    if post is None:
        raise ValueError("Post value cannot be None. You must specify a valid post.")
    if not isinstance(post, PostUpdateDto):
        raise TypeError("Input must be an instance of Post.")

    postData = post_update_entity(post)
    db.update(id, postData)
    return postData



def delete_post(id):
    post = db.get({"_id": ObjectId(id)})
    if post is None:
        raise ValueError("Post value cannot be None. You must specify a valid post.")

    db.delete(id)
    return post_get_entity(post)
