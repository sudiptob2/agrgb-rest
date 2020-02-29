from flask import Flask

app = Flask(__name__)

# Import the Blueprint
from agrgb.api.routes import mod
# Import the site blueprint here if needed
from agrgb.site.routes import mod

# Register the api
app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')
