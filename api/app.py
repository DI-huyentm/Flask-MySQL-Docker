import os
from dotenv import load_dotenv
from flask import Flask

from .db import db
from .migrate import migrate

from . import models

from .resources.book import books as BookBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.url_map.strict_slashes = False  # Disable strict slashes

    # Check if running inside a Docker container
    if os.getenv('DOCKER_CONTAINER') != None:
        # Load .env file in the root directory (for Docker)
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
        load_dotenv(dotenv_path)
        database_url = os.getenv('DATABASE_URL') 
    else:
        # Load .flaskenv file in the api directory (for local development)
        dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
        load_dotenv(dotenv_path)
        database_url = os.getenv('DATABASE_URL_LOCAL') 
        print("flaskenv")

    # Set MySQL database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    migrate.init_app(app, db)
    # api = Api(app)

    with app.app_context():
        db.create_all()

    # Register blueprints with the app
    app.register_blueprint(BookBlueprint, url_prefix='/books')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)