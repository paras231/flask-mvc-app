# app/__init__.py
from flask import Flask
from flaskext.mysql import MySQL
from .config import Config
# import routes for api
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object(Config) 
    # Initialize MySQL
    mysql = MySQL(app)
   # Register Routes
    register_routes(app)
    
    return app
