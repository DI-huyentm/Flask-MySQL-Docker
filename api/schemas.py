from pydantic import BaseModel, Field
from typing import List, Optional


class PlainBookSchema(BaseModel):
    id: int
    title: str
    author: str
    price: int
    image: str
    description: Optional[str] = None  # field can be either a string or None


class BookSchema(PlainBookSchema):
    title: str
    author: str
    price: int
    image: str
    description: Optional[str] = None
    id: Optional[int] = None 

class BookUpdateSchema(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[int] = None
    image: Optional[str] = None
    description: Optional[str] = None


