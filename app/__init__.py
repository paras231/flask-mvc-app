# app/__init__.py
from flask import Flask
import sys
import os
sys.path.append(os.getcwd())
from flaskext.mysql import MySQL
from .config import Config
# import routes for api
from .routes import register_routes
from .models import create_db_tables


def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object(Config) 
    # Initialize MySQL
    mysql = MySQL(app)
    create_db_tables(mysql)
   # Register Routes
    register_routes(app)
    
    return app
