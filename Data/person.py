from app import db

class personForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    telefono = db.Column(db.String(10))