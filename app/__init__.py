from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes import create_routers
from flask_restx import Api
from app.db.database import init_db  # Import init_db

def create_app():
    app = Flask(__name__)

    # Initialize the database
    init_db()

    # Enable CORS for all routes and origins
    CORS(app)

    # Disable masks for optional fields in Swagger
    app.config["RESTX_MASK_SWAGGER"] = False

    api = Api(
        app,
        version="1.0",  # API version
        title="Star Wars API",
        description="A simple Star Wars API",
        doc="/docs",  # Path for Swagger UI documentation
        openapi="3.0.0",  # Specify OpenAPI 3.0
    )

    # Register namespaces after defining the routes
    create_routers(api)

    # Configure Swagger UI
    SWAGGER_URL = "/docs"
    API_URL = "/swagger.json"
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(api.__schema__)

    return app


app = create_app()
