from flask import Flask

app = Flask(__name__)

# Import the Blueprint
# Import the site blueprint here if needed

# Register the api
#app.register_blueprint(app.site.routes.mod)
app.register_blueprint(agrgb.api.routes.mod, url_prefix='/api')
