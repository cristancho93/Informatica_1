from app import db

def create(person):
    db.session.add(person)
    db.session.commit()
    return "Datos Guardados"