from sqlalchemy.orm import Session
from app.modules.characters.models.character_model import Character
from typing import Optional, List  # Necessary import for type annotations


class CharacterRepository:
    """Repository class to handle CRUD operations for characters."""

    def __init__(self, db: Session):
        self.db = db

    def search_all(self) -> List[Character]:
        """Get all characters."""
        return self.db.query(Character).all()

    def search_by_id(self, character_id: int) -> Optional[Character]:
        """Get a character by its ID."""
        return self.db.query(Character).filter(Character.id == character_id).first()

    def add(self, character: Character) -> Character:
        """Add a new character."""
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character

    def delete(self, character_id: int) -> Optional[Character]:
        """Delete a character by its ID."""
        character = self.search_by_id(character_id)
        if character:
            self.db.delete(character)
            self.db.commit()
        return character
