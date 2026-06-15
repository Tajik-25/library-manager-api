from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import datetime
class User(BaseModel):
    email:str
    password:str
class Book(BaseModel):
    title:str
    author:str
    genre:str
    available :bool
class BookUpdate(BaseModel):
    title :Optional[str]=None
    genre:Optional[str] = None
class Book_Response(BaseModel):
    id:int
    title:str
    author:str
    genre:str
    available:bool
    owner_id:int
    created_at:datetime
    model_config = ConfigDict(from_attributes=True)