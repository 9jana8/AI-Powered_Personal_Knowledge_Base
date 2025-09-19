from flask import Blueprint, render_template
from flaskapp.models import Note

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    notes = Note.query.all()
    return render_template('home.html', notes=notes)

@main.route('/about')
def about():
    return render_template('about.html', title='About')