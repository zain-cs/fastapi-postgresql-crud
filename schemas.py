from pydantic import BaseModel
from datetime import datetime

# -------------------------------
# POST SCHEMA (Request)
# -------------------------------
class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True

# -------------------------------
# POST SCHEMA (Response)
# -------------------------------
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    
    class Config:
        from_attributes = True  # For Pydantic v2 (use orm_mode = True for v1)