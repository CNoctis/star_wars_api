from flask_restx import fields


def define_models(api):
    # Define the character model for request
    character_add_params = api.model(
        "Character",
        {
            "id": fields.Integer(required=True, description="Unique ID", example=1),
            "name": fields.String(
                required=True,
                description="Character name",
                example="Luke Skywalker",
                min_length=1,
            ),
            "height": fields.Integer(required=True, description="Height", example=172),
            "mass": fields.Integer(required=True, description="Weight", example=77),
            "hair_color": fields.String(
                required=True, description="Hair color", example="blond", min_length=1
            ),
            "skin_color": fields.String(
                required=True, description="Skin color", example="fair", min_length=1
            ),
            "eye_color": fields.String(
                required=True, description="Eye color", example="blue", min_length=1
            ),
            "birth_year": fields.Integer(
                required=True, description="Birth year", example=1998
            ),
        },
    )

    # Define the character model for response serialization
    character_model_response = api.model(
        "CharacterResponse",
        {
            "id": fields.Integer(description="Unique ID"),
            "name": fields.String(description="Character name"),
            "height": fields.Integer(description="Height"),
            "mass": fields.Integer(description="Weight"),
            "hair_color": fields.String(description="Hair color"),
            "skin_color": fields.String(description="Skin color"),
            "eye_color": fields.String(description="Eye color"),
            "birth_year": fields.Integer(description="Birth year"),
        },
    )

    # Define the error model with meaningful example messages
    error_model = api.model(
        "ErrorResponse",
        {
            "message": fields.String(
                description="Error message", example="An unexpected error occurred."
            ),
        },
    )

    # Define the success message model with meaningful example messages
    success_message_model = api.model(
        "SuccessMessage",
        {
            "message": fields.String(
                description="Success message", example="Character deleted successfully."
            ),
        },
    )

    # Define the character model for the /getAll endpoint
    character_getall_response = api.model(
        "CharacterGetAllResponse",
        {
            "id": fields.Integer(description="Unique ID"),
            "name": fields.String(description="Character name"),
            "height": fields.Integer(description="Height"),
            "mass": fields.Integer(description="Weight"),
            "birth_year": fields.Integer(description="Birth year"),
            "eye_color": fields.String(description="Eye color"),
        },
    )

    return (
        character_add_params,
        character_model_response,
        error_model,
        success_message_model,
        character_getall_response,
    )
