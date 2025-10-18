from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, ValidationError

MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

class UploadForm(FlaskForm):
    file = FileField(
        'Upload File', 
        validators=[
            FileRequired(),
            FileAllowed(['pdf', 'txt', 'md'], 'Only PDF, TXT, or Markdown files allowed!')
            ]
        )
    submit = SubmitField('Upload')

    # Custom validator for file size
    def validate_file(form, field):
        if field.data:
            field.data.stream.seek(0, 2)  # Seek to end of file
            file_size = field.data.stream.tell()
            field.data.stream.seek(0)  # Reset pointer to beginning
            if file_size > MAX_CONTENT_LENGTH:
                raise ValidationError('File size must be under 10 MB.')
