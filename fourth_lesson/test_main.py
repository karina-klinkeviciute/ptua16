import datetime
from http.client import HTTPException
from unittest.mock import MagicMock

import pytest
from fastapi import FastAPI, Depends, HTTPException
from fastapi.testclient import TestClient
from requests.sessions import Session

from .models import Author
from .main import app
from .database import get_db
from pydantic import BaseModel
from typing import Optional

class AuthorResponse(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    date_of_birth: str


# # Mock database dependency
# def mock_get_db():
#     db = MagicMock()
#
#     cursor = MagicMock()
#     db.cursor.return_value = cursor
#
#     # Simulate the cursor's fetchone behavior
#     cursor.fetchone.side_effect = [
#         {"id": 1, "first_name": "Margaret", "last_name": "Atwood"},  # Simulate a successful fetch for ID 1
#         None  # Simulate a failed fetch for other IDs
#     ]
#
#     return db
#
#
#
# app.dependency_overrides[get_db] = mock_get_db



def test_create_author_bad_payload():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/authors/", json={"name": "George Orwell"})
        assert response.status_code == 422
        # assert response.json()["name"] == "George Orwell"

def test_create_author_success():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/authors/", json={
            "first_name": "George",
            "last_name": "Orwell",
            "date_of_birth": "1903-06-25"
        })
        assert response.status_code == 201
        assert "id" in response.json().keys()
        assert response.json()["first_name"] == "George"
        assert response.json()["last_name"] == "Orwell"
        assert response.json()["date_of_birth"] == "1903-06-25"

def test_retrieve_author_success():
    # birth_date = datetime.datetime.strptime('1939-11-18', "%Y-%m-%d").date()
    # new_author = Author(first_name="Margaret", last_name="Atwood", date_of_birth=birth_date)
    # try:
    #     db: Session = get_db()
    #     db.add(new_author)
    #     db.commit()
    #     db.refresh(new_author)  # Refresh to get the generated ID
    #     print(new_author)
    # except Exception as e:
    #     # db.rollback()
    #     print("error")

    with TestClient(app=app, base_url="http://test") as client:
        response_created = client.post("/authors/", json={
            # "id": 1,
            "first_name": "Margaret",
            "last_name": "Atwood",
            "date_of_birth": "1939-11-18"
        })


    with TestClient(app=app, base_url="http://test") as client:
        response = client.get(f"/authors/{response_created.json()['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == response_created.json()['id']
        assert response.json()["first_name"] == "Margaret"
        assert response.json()["last_name"] == "Atwood"
        assert response.json()["date_of_birth"] == "1939-11-18"


def test_create_book_bad_payload():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/books/", json={"title": "The Hobbit"})
        assert response.status_code == 422

def test_create_book_success():
    with TestClient(app=app, base_url="http://test") as client:
        author_response = client.post("/authors/", json={
            "first_name": "George",
            "last_name": "Orwell",
            "date_of_birth": "1903-06-25"
        })

        assert author_response.status_code == 201

    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/books/", json={
            "title": "The Hobbit",
            "release_year": "1937-01-01",
            "author_id": author_response.json()["id"]
        })
        # created_book_id = response.json()["id"]
        assert response.status_code == 201
        assert "id" in response.json().keys()
        # assert response.json()["id"] == created_book_id
        assert response.json()["title"] == "The Hobbit"
        assert response.json()["release_year"] == "1937-01-01"
        assert response.json()["author"] == {
            "id": author_response.json()["id"],
            "first_name": "George",
            "last_name": "Orwell",
            "date_of_birth": "1903-06-25"
        }

def test_retrieve_all_books_success():
    with TestClient(app=app, base_url="http://test") as client:
        author_response = client.post("/authors/", json={
            "first_name": "George",
            "last_name": "Orwell",
            "date_of_birth": "1903-06-25"
        })

        assert author_response.status_code == 201

    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/books/", json={
            "title": "The Hobbit",
            "release_year": "1937-01-01",
            "author_id": author_response.json()["id"]
        })

    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/books/", json={
            "title": "The Hobbit",
            "release_year": "1937-01-01",
            "author_id": author_response.json()["id"]
        })

    with TestClient(app=app, base_url="http://test") as client:
        books_response = client.get("/books/")
        assert books_response.status_code == 200
        print(books_response.json())
        assert len(books_response.json()["books"]) > 1
