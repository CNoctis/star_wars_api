def serialize_character(character):
    """Converts a SQLAlchemy Character object into a serializable dictionary."""
    return {
        "id": character.id,
        "name": character.name,
        "height": character.height,
        "mass": character.mass,
        "hair_color": character.hair_color,
        "skin_color": character.skin_color,
        "eye_color": character.eye_color,
        "birth_year": character.birth_year,
    }
