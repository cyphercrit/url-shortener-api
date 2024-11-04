from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2000), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
