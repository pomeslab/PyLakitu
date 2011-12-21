import flask

app = flask.Flask(__name__)

from PyLakitu.database import db_session
import PyLakitu.views

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
