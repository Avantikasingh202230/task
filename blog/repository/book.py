from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from ..models import *

def get_all(db: Session):
    blogs = db.query(models.Book).all()
    return blogs

def create(request: Book,db: Session):
    new_blog = models.Book(name=request.name, date=request.date,user_id=request.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog = db.query(models.Book).filter(models.Book.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:Book, db:Session):
    blog = db.query(models.Book).filter(models.Book.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog = db.query(models.Book).filter(models.Book.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog