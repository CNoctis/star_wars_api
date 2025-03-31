from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Character(Base):
    """
    Data model to represent a Star Wars character.

    Attributes:
        id (int): Unique ID of the character.
        name (str): Name of the character.
        height (int): Height of the character in centimeters.
        mass (int): Weight of the character in kilograms.
        hair_color (str): Hair color of the character.
        skin_color (str): Skin color of the character.
        eye_color (str): Eye color of the character.
        birth_year (int): Birth year of the character.
    """

    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
