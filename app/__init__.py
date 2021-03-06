import os
from flask import Flask
from flask_cors import CORS

# Initialize application
app = Flask(__name__, static_folder=None)

# Enabling cors
CORS(app)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

# Import the application views
from app import views

# Register blue prints
from app.users.views import users

app.register_blueprint(users, url_prefix='/v1')

from app.groups.views import groups

app.register_blueprint(groups, url_prefix='/v1')

from app.docs.views import docs

app.register_blueprint(docs)