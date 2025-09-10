from app import db
from datetime import datetime

class Note(db.Model):
    __tablename__ = "notes"