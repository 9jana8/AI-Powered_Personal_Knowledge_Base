'''__init__.py tells Python this is a package. Creates the Flask app + db.'''
from flask import Flask
import secrets
import os
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskapp import routes