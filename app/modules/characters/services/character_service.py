from sqlalchemy.orm import Session
from app.modules.characters.models.character_model import Character
from app.modules.characters.repositories.character_repository import CharacterRepository
from typing import Optional, List  # Import necesario para anotaciones de tipo


class CharacterService:
    """Service class to handle business logic for characters."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = CharacterRepository(db)

    def search_all(self) -> List[Character]:
        return self.repository.search_all()

    def search_by_id(self, character_id: int) -> Optional[Character]:
        return self.repository.search_by_id(character_id)

    def create(self, character_data: dict) -> Character:
        if self.repository.search_by_id(character_data["id"]):
            raise ValueError("Character with this ID already exists.")
        character = Character(**character_data)
        return self.repository.add(character)

    def remove(self, character_id: int) -> Character:
        character = self.repository.search_by_id(character_id)
        if not character:
            raise ValueError("Character not found.")
        return self.repository.delete(character_id)
