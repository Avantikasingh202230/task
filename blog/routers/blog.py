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
router= APIRouter(prefix='/blog',tags=['Blog'])

#tag define the proper documentation of a particualr syastem.different different route for user as well as for blogs.wrapping and unrapping of the route is possible
models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close
# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create_blog(request:Blog, db:Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

#to display all the fields of the complete blog table
# @app.get('/blog')
# def all(db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

#to display all the information from a particular blog
# @app.get('/blog/{id}')
# def show(id, response:Response,db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id==id).all()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'details':f'Blog with the id {id} not found'}
#     return blogs
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
    
    #if you want to update a single field of the database
    blog.delete({'title':'updated title', 'body':'updated body'})
    db.commit()
    return "done"
    # db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    # db.commit()
    # return {"status": "the blog is deleted"}

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog, db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:Blog, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
    
    #if you want to update a single field of the database
    blog.update({'title':'updated title', 'body':'updated body'})
    db.commit()
    return "done"
#to hide any information in the get method
@router.get('/{id}', status_code=200,response_model=ShowBlog)
def show(id, response:Response,db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'details':f'Blog with the id {id} not found'}
    return blogs

#to get all the list of the post with title only
@router.get('/', response_model=List[ShowBlog])
def add(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

# to create a user
# @app.post('/user')
# def create_user(request:User,db:Session=Depends(get_db)):
#     new_user=models.User(name=request.name, email=request.email,password=request.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

#user creation with password hashing
# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

#user creation that returmn id,name,email,password
# @app.post('/user')
# def create_user(request:User,db:Session=Depends(get_db)):
#     # hashedPassword= pwd_cxt.hash(request.password)
#     new_user=models.User(name=request.name, email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user