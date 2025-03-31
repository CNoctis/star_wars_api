from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./app/star_wars.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db() -> None:
    """
    Initializes the database by creating all tables defined in the models.
    """
    from app.modules.characters.models.character_model import Character

    # Create all tables in the database
    Base.metadata.create_all(bind=engine)
