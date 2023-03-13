from pydantic import BaseModel
from typing import List
class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True
# class Blog(BaseModel):
#     title:str
#     body:str
#     class Config():
#         orm_mode=True
#to display any particular field we use class config  it is a response model
# class ShowBlog(BaseModel):
#     title:str
#     class Config():
#         orm_mode=True
    
#to create a user
class User(BaseModel):
    name:str
    email:str
    password:str
#response body for user
class ShowUser(BaseModel):
    name:str
    email:str
    blogs :List[Blog]=[]
    # blogs:List
    # #we are getting name,email,everything of the blog with all the fields
    class Config():
        orm_mode=True
#to display any particular field we use class config  it is a response model
#here we define a new ShowBlog to fetch the information of the user with the particular blog
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode=True
    