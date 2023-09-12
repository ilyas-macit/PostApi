from pydantic import BaseModel
from typing import List
from datetime import datetime
class Post(BaseModel):
    id: str
    title: str
    short_description: str
    description: str
    tags: List[str]
    created_at: datetime
    updated_at: datetime
