from sqlalchemy import Column, Integer, String, ForeignKey, Date
from blog.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

import datetime
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id')) #relationship

    creator = relationship("User", back_populates="books")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    books = relationship('Book', back_populates="creator") #relationshit