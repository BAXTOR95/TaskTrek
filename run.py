import os
from flask import Flask
from models.database import db
from config import Config
from extensions import init_app

PROD = True if os.environ.get('PROD', False) == 'True' else False


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)  # Initialize Flask extensions

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=not PROD)
