from .schemas import AuthorResponse, BookResponse, AuthorCreate, BookCreate
from .models import Author, Book
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db


app = FastAPI()

@app.get("/authors")
def get_all_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    return {"authors": authors}

@app.get("/books")
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return {"books": books}

@app.get("/authors/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int , db: Session = Depends(get_db)):
    try:
        author = db.query(Author).filter_by(id = author_id).first()

        return {"id": author.id, "first_name" : author.first_name, "last_name": author.last_name, "date_of_birth": author.date_of_birth}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int , db: Session = Depends(get_db)):
    try:
        book = db.query(Book).filter_by(id = book_id).first()

        return {"id": book.id, "title" : book.title, "release_year": book.release_year,
                "author": {
                "id": book.author.id,
                "first_name" : book.author.first_name,
                "last_name" : book.author.last_name,
                "date_of_birth" : book.author.date_of_birth
            }}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/authors", response_model=AuthorResponse, status_code=201)
def create_author(user: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(first_name = user.first_name, last_name= user.last_name, date_of_birth=user.date_of_birth)
    try:
        db.add(new_author)
        db.commit()
        db.refresh(new_author) #Refresh to get the generated ID
        return {
            "id": new_author.id,
            "first_name": new_author.first_name,
            "last_name": new_author.last_name,
            "date_of_birth": new_author.date_of_birth
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(title = book.title,
                    release_year= book.release_year,
                    author_id=book.author_id)
    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book) #Refresh to get the generated ID
        return {
            "id": new_book.id,
            "title": new_book.title,
            "release_year": new_book.release_year,
            "author": {
                "id": new_book.author.id,
                "first_name" : new_book.author.first_name,
                "last_name" : new_book.author.last_name,
                "date_of_birth" : new_book.author.date_of_birth
            }
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))