import os
from flask import Flask

from fpl_optimizer.db import init_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_db(app)

    @app.route("/")
    def index():
        return """
        <h1>Fantasy Premier League Optimizer</h1>
        <p>Generate your FPL team automatically based on your selection of parameters</p>
        """

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
