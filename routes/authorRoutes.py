from fastapi import APIRouter, HTTPException
from controllers.authorCotroller import (
    create_author, get_authors, get_author, update_author, delete_author
)
from models.author import Author, AuthorInDB

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}

@router.post("/author", response_model=AuthorInDB)
async def create_author_route(author: Author):
    return await create_author(author)

@router.get("/authors", response_model=list[AuthorInDB])
async def get_authors_route():
    return await get_authors()

@router.get("/author/{author_id}", response_model=AuthorInDB)
async def get_author_route(author_id: str):
    return await get_author(author_id)

@router.put("/author/{author_id}", response_model=AuthorInDB)
async def update_author_route(author_id: str, author: Author):
    return await update_author(author_id, author)

@router.delete("/author/{author_id}", response_model=AuthorInDB)
async def delete_author_route(author_id: str):
    return await delete_author(author_id)
