import os
from flask import Flask

app = Flask(__name__)

# required to launch the flask app
# TODO what should be the right secret?
app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))

from webapp.core.views import core

app.register_blueprint(core)