from datetime import date
from pydantic import BaseModel


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth : date

class AuthorResponse(BaseModel):
    id : int
    first_name: str
    last_name: str
    date_of_birth : date

class BookCreate(BaseModel):
    title: str
    release_year: date
    author_id: int

class BookResponse(BaseModel):
    id: int
    title: str
    release_year: date
    author: AuthorResponse