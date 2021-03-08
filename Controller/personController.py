from app import *

def create(person):
    db.session.add(person)
    db.session.commit()
    return "Datos Guardados"

def lista():
    persons = personForm.query.all()
    return persons