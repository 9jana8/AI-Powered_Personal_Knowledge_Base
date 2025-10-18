'''__init__.py tells Python this is a package. Creates the Flask app + db.'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskapp.config import Config
from markupsafe import Markup
import re

# Initialize Flask app extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Creates and configures Flask app instance
def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from flaskapp.models import User
        from flaskapp.models import Note
        from flaskapp.models import Document
        db.create_all()

    from flaskapp.users.routes import users
    from flaskapp.notes.routes import notes
    from flaskapp.main.routes import main
    from flaskapp.uploads.routes import uploads
    app.register_blueprint(users)
    app.register_blueprint(notes)
    app.register_blueprint(main)
    app.register_blueprint(uploads)
    
    app.jinja_env.filters['highlight'] = highlight_search

    return app

# Helper function to highlight the text that matches a search query
def highlight_search(text, query):
    if not query:
        return text
    
    pattern = re.compile(re.escape(query), re.IGNORECASE)

    def replace_match(match):
        return f"<mark>{match.group(0)}</mark>"

    highlighted = pattern.sub(replace_match, text)
    return Markup(highlighted)