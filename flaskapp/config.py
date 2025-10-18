import os

BASE_DIR = r'C:\Users\jana.sosic\OneDrive - Accenture\Desktop\Privatno\AI-Powered_Personal_Knowledge_Base\flaskapp'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploaded_docs')
