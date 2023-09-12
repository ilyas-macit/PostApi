from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Post(BaseModel):
    title: str = None
    short_description: str = None
    description: str = None
    tags: List[str] = None
    created_at: datetime = None
    updated_at: datetime = None


class PostUpdateDto(BaseModel):
    title: str = None
    short_description: str = None
    description: str = None
    tags: List[str] = None

