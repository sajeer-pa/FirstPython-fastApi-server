from pydantic import BaseModel

class Author(BaseModel):
    name: str
    age: int

class AuthorInDB(Author):
    id: str