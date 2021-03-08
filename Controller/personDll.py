from app import db

def create(person):
    db.session.add(person);
    db.session.commi();
    return 'Datos Guardados';