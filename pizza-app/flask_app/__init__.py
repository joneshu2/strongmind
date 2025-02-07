"""
Author: Hunter Jones
"""

import os
from flask import Flask
from flask_failsafe import failsafe


# Create app and output entry point in return
# App factory wrapped with failsafe decorator to return fallback app displaying Flask error debugger
@failsafe
def create_app(debug=False):
  # Initialize Flask application instance
  app = Flask(__name__)

  # Cached static file fix for some issues, consider changing to help improce performance
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.debug = debug

  # Secret Key for signing, switch to different environment variable once further along for deployment 
  app.secret_key = 'strongmindpizza'

  with app.app_context():
    from . import routes
    return app
