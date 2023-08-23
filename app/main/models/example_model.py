from .. import db

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(64))