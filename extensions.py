import os
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from models.database import db
from dotenv import load_dotenv
from pathlib import Path

# Initialize environment variables
ENV_PATH = Path(".env")
load_dotenv(dotenv_path=ENV_PATH)

# Initialize Flask extensions
login_manager = LoginManager()
bootstrap = Bootstrap5()
migrate = Migrate()


def init_app(app):
    """Initialize Flask application."""
    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'

    bootstrap.init_app(app)
