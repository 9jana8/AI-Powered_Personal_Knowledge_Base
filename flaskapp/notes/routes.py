from flask import render_template, url_for, redirect, flash, abort, request, Blueprint
from flaskapp import db
from flaskapp.notes.forms import NoteForm
from flaskapp.models import Note
from flask_login import current_user, login_required

notes = Blueprint('notes', __name__)

@notes.route('/note/new', methods=['GET', 'POST'])
@login_required
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Your note was created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_and_update_note.html', title='New Note', form=form, legend='Create a Note')

@notes.route('/note/<int:note_id>')
@login_required
def note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', title=note.title, note=note)

@notes.route('/note/<int:note_id>/update', methods=['GET', 'POST'])
@login_required
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        db.session.commit()
        flash('Your note was updated!', 'success')
        return redirect(url_for('notes.note', note_id=note.id))
    elif request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.content
    return render_template('create_and_update_note.html', title='Update Note', form=form, legend='Update a Note')

@notes.route('/note/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    db.session.delete(note)
    db.session.commit()
    flash('Your note has been deleted!', 'success')
    return redirect(url_for('main.home'))

@notes.route('/notes')
@login_required
def list_notes():
    query = request.args.get('q', '')
    if query:
        notes_list = Note.query.filter(
            Note.author == current_user,
            (Note.title.ilike(f'%{query}%')) | (Note.content.ilike(f'%{query}%'))
        ).all()
    else:
        notes_list = Note.query.filter(Note.author == current_user).all()

    return render_template('list_notes.html', notes=notes_list, query=query)