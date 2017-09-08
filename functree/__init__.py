import flask, flask_mongoengine, flask_wtf.csrf, flask_httpauth, flask_debugtoolbar, subprocess

app = flask.Flask(__name__, instance_relative_config=True)
app.config.from_object('functree.config')
app.config.from_pyfile('config.py', silent=True)

db = flask_mongoengine.MongoEngine(app)
csrf = flask_wtf.csrf.CSRFProtect(app)
auth = flask_httpauth.HTTPDigestAuth()
toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

app.session_interface = flask_mongoengine.MongoEngineSessionInterface(db)

with app.app_context():
    try:
        version = subprocess.check_output(['git', 'describe', '--long']).decode('utf-8')
    except subprocess.CalledProcessError:
        version = 'v(N/A)'
    flask.current_app.version = version

import functree.views
