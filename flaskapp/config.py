import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#BASE_DIR = r'/home/jana/src/AI-Powered_Personal_Knowledge_Base/flaskapp'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///site.db'
    )
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploaded_docs')
