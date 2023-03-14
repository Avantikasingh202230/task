from pydantic import BaseModel
from datetime import datetime, timezone
from typing import List, Optional
from datetime import date
from datetime import datetime
class BlogBase(BaseModel):
    name: str
    date: date
    id:int

class Book(BlogBase):
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
    books :List[Book]=[]
    # blogs:List
    # #we are getting name,email,everything of the blog with all the fields
    class Config():
        orm_mode=True
#to display any particular field we use class config  it is a response model
#here we define a new ShowBlog to fetch the information of the user with the particular blog
class ShowBook(BaseModel):
    name:str
    # date:datetime
    # creator:ShowUser
    class Config():
        orm_mode=True

#login
class Login(BaseModel):
    username: str
    password:str
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None