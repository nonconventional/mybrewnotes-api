from app.api import bp as api_bp
from app import routes
import os
from flask import Flask
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# app.config.from_object("config.DevelopmentConfig")


app.register_blueprint(api_bp, url_prefix='/api')
