from typing import Dict, Any  # Necessary import for type annotations

def validate_character_data(data: Dict[str, Any]) -> None:
    """
    Validates the data to create or update a character.

    Args:
        data (Dict[str, Any]): Dictionary with the character's data.

    Raises:
        ValueError: If any required field is missing or if a field has an incorrect type.
    """
    required_fields = {
        "id": int,
        "name": str,
        "height": int,
        "mass": int,
        "hair_color": str,
        "skin_color": str,
        "eye_color": str,
        "birth_year": int,
    }

    for field, field_type in required_fields.items():
        if field not in data or not data[field]:
            raise ValueError(f"The field '{field}' is required and cannot be null or empty.")
        if not isinstance(data[field], field_type):
            raise ValueError(f"The field '{field}' must be of type {field_type.__name__}.")
