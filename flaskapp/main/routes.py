from flask import Blueprint, render_template
from flaskapp.models import Note, Document
from flaskapp.uploads.forms import UploadForm
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    notes = Note.query.all()
    form = UploadForm() if current_user.is_authenticated else None
    documents = Document.query.filter_by(user_id=current_user.id).all() if current_user.is_authenticated else []
    return render_template('home.html', notes=notes, form=form, documents=documents)

@main.route('/about')
def about():
    return render_template('about.html', title='About')