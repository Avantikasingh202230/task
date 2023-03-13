from blog.schemas import *
from passlib.context import CryptContext
from fastapi import FastAPI,Depends, status, Response, HTTPException
from pydantic import BaseModel
from blog.schemas import Blog
from .. import  models
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash
from fastapi import APIRouter,Depends,status,HTTPException
router= APIRouter(prefix='/user',tags=['User'])


#tag define the proper documentation of a particualr syastem.different different route for user as well as for blogs.wrapping and unrapping of the route is possible
models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close




@router.post('/', response_model=ShowUser)
def create_user(request:User,db:Session=Depends(get_db)):
    # hashedPassword= pwd_cxt.hash(request.password)
    new_user=models.User(name=request.name, email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get('/{id}', response_model=ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User  with the id {id} not found')
    return user
