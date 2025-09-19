'''__init__.py tells Python this is a package. Creates the Flask app + db.'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskapp.config import Config

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

with app.app_context():
    from flaskapp.models import User
    from flaskapp.models import Note
    db.create_all()

from flaskapp.users.routes import users
from flaskapp.notes.routes import notes
from flaskapp.main.routes import main

app.register_blueprint(users)
app.register_blueprint(notes)
app.register_blueprint(main)

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)