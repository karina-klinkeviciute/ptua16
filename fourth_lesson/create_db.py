from database import engine, Base
from models import Author,Book    #IMPORTANT TO CREATE TABLES!


def create_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db()