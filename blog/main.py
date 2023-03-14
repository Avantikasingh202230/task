from .routers import book, user, authentication
from blog.schemas import *
from passlib.context import CryptContext
from fastapi import FastAPI,Depends, status, Response, HTTPException
from pydantic import BaseModel
from blog.schemas import Book
from . import  models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
app=FastAPI()
app.include_router(book.router)
app.include_router(user.router)
app.include_router(authentication.router)

#tag define the proper documentation of a particualr syastem.different different route for user as well as for blogs.wrapping and unrapping of the route is possible
models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close