# import uvicorn
# from fastapi import FastAPI, HTTPException
# from fastapi_sqlalchemy import DBSessionMiddleware, db
# from pydantic import BaseModel


# from schema import Book as SchemaBook
# from schema import Author as SchemaAuthor

# from models import Book as ModelBook
# from models import Author as ModelAuthor

# import os
# from dotenv import load_dotenv

# load_dotenv('.env')

# app = FastAPI()

# # Add middleware for database session management
# app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# @app.get("/")
# async def root():
#     return {"message": "hello world"}


# @app.post('/book/', response_model=SchemaBook)
# async def book(book: SchemaBook):
#     db_book = ModelBook(title=book.title, rating=book.rating, author_id = book.author_id)
#     db.session.add(db_book)
#     db.session.commit()
#     return db_book

# @app.get('/book/')
# async def book():
#     book = db.session.query(ModelBook).all()
#     return book

# class Author(BaseModel):
#     name: str
#     age: int
  
# @app.post('/author')
# async def create_author(author: Author):
#     db_author = ModelAuthor(name=author.name, age=author.age)
#     db.session.add(db_author)
#     db.session.commit()
#     return db_author



# @app.post("/author/")
# async def create_author(author: Author):
#     # Process the author object
#     # Example: Save to database or perform operations
#     # Return a response with the author's details
#     return {"message": f"User created with name {author.name}"}

# @app.get('/author/')
# async def author():
#     author = db.session.query(ModelAuthor).all()
#     return author


# # To run locally
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)




# main.py

# import os
# from fastapi import FastAPI
# from fastapi_sqlalchemy import DBSessionMiddleware, db
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Load environment variables
# from dotenv import load_dotenv
# load_dotenv('.env')

# # PostgreSQL database URL from environment variable
# DATABASE_URL = os.environ['DATABASE_URL']
# print(f"Loaded DATABASE_URL: {DATABASE_URL}")


# # SQLAlchemy configuration
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # FastAPI app
# app = FastAPI()

# # Middleware for SQLAlchemy session management
# app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

# @app.get("/")
# async def root():
#     return {"message": "hello world"}
# # Example SQLAlchemy model
# class Author(Base):
#     __tablename__ = 'author'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)

# # Example API endpoint
# @app.post('/author')
# async def create_author(name: str, age: int):
#     db_author = Author(name=name, age=age)
#     db.session.add(db_author)
#     db.session.commit()
#     db.session.refresh()

#     return db_author




import os
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from schema import Publication as SchemaPublication
from schema import Author as SchemaAuthor

from models import Publication as ModelPublication
from models import Author as ModelAuthor

# Load environment variables
from dotenv import load_dotenv
load_dotenv('.env')

# PostgreSQL database URL from environment variable
DATABASE_URL = os.environ['DATABASE_URL']

# SQLAlchemy configuration
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI app
app = FastAPI()

# Middleware for SQLAlchemy session management
app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

# Example SQLAlchemy model
# class Author(Base):
#     __tablename__ = 'author'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)

# # Create tables in the database (if not already created)
# Base.metadata.create_all(bind=engine)

# Example API endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/author')
async def create_author(auth :SchemaAuthor):
    db_author = ModelAuthor(name=auth.name, age=auth.age)
    db.session.add(db_author)
    db.session.commit()
    db.session.refresh(db_author)
    return db_author


