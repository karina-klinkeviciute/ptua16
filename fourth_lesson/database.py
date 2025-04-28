from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the SQLite URL for synchronous access
DATABASE_URL = "postgresql://ptua16:test@localhost:5432/ptua16"
TEST_DATABASE_URL = "postgresql://ptua16:test@localhost:5432/ptua16"


# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for declarative models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()