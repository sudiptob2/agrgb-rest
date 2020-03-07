from flask import Flask

from .api.routes import mod


app = Flask(__name__)

# Import the Blueprint
# Import the site blueprint here if needed

# Register the api
app.register_blueprint(mod, url_prefix='/api')
