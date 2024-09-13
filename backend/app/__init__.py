from flask import Flask
from flask_cors import CORS
from app.routes import main_bp, hello_bp

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object('config.Config')

    # Initialize CORS
    CORS(app)

    # Register routes blueprint
    app.register_blueprint(main_bp)
    app.register_blueprint(hello_bp)


    return app
