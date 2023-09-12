from routers.post_router import posts
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()
app.include_router(posts)


run(app)



