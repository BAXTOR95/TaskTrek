import os
from flask import Flask
from web.routes import web_blueprint
from config import Config
from extensions import init_app
from flask_migrate import upgrade
import web.services.auth.auth

PROD = True if os.environ.get('PROD', False) == 'True' else False


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)  # Initialize Flask extensions

    # Ensure the application context is available for the upgrade operation
    with app.app_context():
        upgrade()  # Automatically apply migrations at startup

    app.register_blueprint(web_blueprint, url_prefix="/")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=not PROD)
