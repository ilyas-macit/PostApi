from fastapi import APIRouter, HTTPException
from models.post import Post
from services.post_service import *

posts = APIRouter()


@posts.get("/posts/")
def get_all_post():
    try:
        return get_all()
    except Exception as e:
        return HTTPException(status_code= 400, detail= str(e))

@posts.get("/posts/{id}")
def get_post_by_id(id):
    try:
        return get_by_id(id)
    except Exception as e:
        return HTTPException(status_code= 400, detail= str(e))

@posts.post("/posts/")
def create(post : Post):
    try:
        create_post(post)
    except Exception as e:
        return HTTPException(status_code= 400, detail= str(e))



@posts.put("/posts/{id}")
def update(id, post: PostUpdateDto):
    try:
        post = update_post(id,post)
        return post
    except Exception as e:
        return HTTPException(status_code= 400, detail= str(e))


@posts.delete("/posts/{id}")
def delete(id):
    try:
        delete_post(id)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
