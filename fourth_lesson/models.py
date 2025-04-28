from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    date_of_birth = Column(Date)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column("title", String)
    release_year = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")