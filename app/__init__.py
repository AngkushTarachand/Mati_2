import flask
# import flask_login
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
flask_app = flask.Flask(__name__)
# secret key for form
flask_app.config['SECRET_KEY'] = "final"
# configuration of database
flask_app.config.from_object(Config)
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)
# login_manager = flask_login.LoginManager(flask_app)
from app import routes, models
