from sqlalchemy import Integer,String,Column,ForeignKey,DateTime,BOOLEAN
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    books = relationship("Books",back_populates="user")
class Books(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    title=Column(String)
    author = Column(String)
    genre = Column(String)
    available = Column(BOOLEAN)
    owner_id = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime,default=datetime.utcnow())
    user = relationship("Users",back_populates="books")
    