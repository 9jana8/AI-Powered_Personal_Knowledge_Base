from flask import render_template, url_for, redirect, flash, request, Blueprint, current_app, send_from_directory
from flaskapp import db
from flaskapp.uploads.forms import UploadForm
from flaskapp.models import Document
import os, secrets
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge


uploads = Blueprint('uploads', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'md'}  # set (vs list, vs dict)

@uploads.errorhandler(RequestEntityTooLarge)
def handle_large_file(e):
    flash('File is too large! Maximum allowed size is 10 MB.', 'danger')
    return redirect(url_for('uploads.upload_file'))

def allowed_file(filename: str) -> bool:
    good_extension = filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    dot_in_name = '.' in filename
    return good_extension and dot_in_name


@uploads.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = UploadForm()
    print("Form submitted:", request.method, form.validate_on_submit())
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)

        if not allowed_file(filename):
            flash('Invalid file type. Allowed types: pdf, txt, md', 'danger')
            return redirect(url_for('uploads.upload_file'))

        random_hex = secrets.token_hex(8)
        _, extension = os.path.splitext(filename)
        stored_name = random_hex + extension

        os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], stored_name)
        file.save(save_path)
        
        doc = Document(
            filename=filename, 
            stored_name=stored_name, 
            status='Uploaded',
            user_id=current_user.id
        )
        db.session.add(doc)
        db.session.commit()

        flash('File uploaded successfully!', 'success')
        return redirect(url_for('uploads.upload_file'))
    
    documents = Document.query.filter_by(user_id=current_user.id).all()
    return render_template('upload_document.html', form=form, documents=documents)

@uploads.route('/upload/<filename>')
@login_required
def view_document(filename):
    """Serve uploaded file for viewing or downloading"""
    return send_from_directory(
        current_app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=False
    )

@uploads.route('/upload/delete/<int:doc_id>', methods=['POST'])
@login_required
def delete_document(doc_id):
    doc = Document.query.get_or_404(doc_id)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], doc.stored_name)

    if os.path.exists(filepath):
        os.remove(filepath)

    db.session.delete(doc)
    db.session.commit()
    flash('File is deleted successfully', 'success')
    return redirect(url_for('uploads.upload_file'))

    