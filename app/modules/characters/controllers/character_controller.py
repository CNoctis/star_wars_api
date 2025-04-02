from flask_restx import Resource
from flask import request
from app.modules.characters import ns_characters
from app.db.database import SessionLocal
from app.modules.characters.controllers.utils.serialize_character import (
    serialize_character,
)
from app.modules.characters.services.character_service import CharacterService
from app.modules.characters.controllers.utils.models import define_models
from app.modules.characters.controllers.utils.validators import validate_character_data

db = SessionLocal()
service = CharacterService(db)  # Initialize the service with the database session

# Rename the namespace to avoid confusion
api = ns_characters

# Define models for request and response
(
    character_add_params,
    character_model_response,
    error_model,
    success_message_model,
    character_getall_response,
) = define_models(api)


@api.route("/getAll")
class CharacterListResource(Resource):
    @api.doc(
        description="Get all characters.",
        responses={
            200: ("Success", [character_getall_response]),
            500: ("Internal Server Error", error_model),
        },
    )
    @api.marshal_list_with(character_getall_response)
    def get(self):
        characters = service.search_all()
        return characters, 200


@api.route("/get/<int:id>")
class CharacterResource(Resource):
    @api.doc(
        description="Get a character by ID.",
        responses={
            200: ("Success", character_model_response),
            404: ("Character not found", error_model),
            500: ("Internal Server Error", error_model),
        },
    )
    @api.marshal_with(character_model_response)
    def get(self, id):
        character = service.search_by_id(id)
        if not character:
            api.abort(404, "Character not found.")
        return serialize_character(character), 200


@api.route("/add")
class AddCharacterResource(Resource):
    @api.expect(character_add_params)
    @api.doc(
        description="Add a new character.",
        responses={
            200: ("Character created successfully", character_model_response),
            400: ("Invalid request data", error_model),
            500: ("Internal Server Error", error_model),
        },
    )
    @api.marshal_with(character_model_response)
    def post(self):
        data = request.json
        try:
            # Validate the incoming data
            validate_character_data(data)
            character = service.create(data)
            return serialize_character(character), 200
        except ValueError as e:
            api.abort(400, str(e))


@api.route("/delete/<int:id>")
class DeleteCharacterResource(Resource):
    @api.doc(
        description="Delete a character by ID.",
        responses={
            200: ("Character deleted successfully", success_message_model),
            400: ("Invalid request or character not found", error_model),
            500: ("Internal Server Error", error_model),
        },
    )
    @api.marshal_with(success_message_model, code=200)
    def delete(self, id):
        try:
            service.remove(id)
            return {"message": "Character deleted successfully."}, 200
        except ValueError as e:
            api.abort(400, str(e))
