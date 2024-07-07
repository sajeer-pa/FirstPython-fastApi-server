from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from database import mongodb
from models.author import Author, AuthorInDB

async def create_author(author: Author):
    author_dict = author.dict()
    result = await mongodb.db.authors.insert_one(author_dict)
    author_dict["id"] = str(result.inserted_id)
    return author_dict

async def get_authors():
    authors = await mongodb.db.authors.find().to_list(1000)
    for author in authors:
        author["id"] = str(author["_id"])
    return authors

async def get_author(author_id: str):
    author = await mongodb.db.authors.find_one({"_id": ObjectId(author_id)})
    if author:
        author["id"] = str(author["_id"])
    return author

async def update_author(author_id: str, author: Author):
    update_result = await mongodb.db.authors.update_one(
        {"_id": ObjectId(author_id)}, {"$set": author.dict()}
    )
    if update_result.modified_count == 1:
        updated_author = await mongodb.db.authors.find_one({"_id": ObjectId(author_id)})
        updated_author["id"] = str(updated_author["_id"])
        return updated_author

async def delete_author(author_id: str):
    delete_result = await mongodb.db.authors.delete_one({"_id": ObjectId(author_id)})
    if delete_result.deleted_count == 1:
        return {"id": author_id}
