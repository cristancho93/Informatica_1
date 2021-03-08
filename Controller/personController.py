from app import db, personForm
from sqlalchemy import desc


def lista():
    persons = personForm.query.order_by(desc('id')).all()
    return persons


def create(person):
    db.session.add(person)
    db.session.commit()
    return "Datos Guardados"


def delete(id):
    personForm.query.filter_by(id=int(id)).delete()
    db.session.commit()


def update(person):
    persona = personForm.query.filter_by(id=int(person.id)).first()
    persona.nombre = person.nombre
    persona.apellido = person.apellido
    persona.telefono = person.telefono
    db.session.commit()
