import os
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from google.cloud import firestore

app = Flask(__name__)
Bootstrap(app)

# required to launch the flask app
# TODO what should be the right secret?
app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))
firestore_storedb = firestore.Client()

location_id = 0

from webapp.core.views import core
from webapp.location.views import locations

app.register_blueprint(core)
app.register_blueprint(locations)