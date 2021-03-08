from flask import url_for, redirect
from Controller.personController import create, update, delete, lista


def saveItem(person):
    validation = False
    if person.nombre and person.apellido and person.telefono:
        validation = True
    else:
        validation = False

    if validation:
        create(person)
        if(person.id is None):
            return "Error al guardar"
        else:
            return redirect(url_for('home'))
    else:
        return "Revise que los campos del formulario esten diligenciados"

def updateItem(person):
    update(person)
    return redirect(url_for('home'))


def deleteItem(id):
    delete(id)
    return redirect(url_for('home'))


def listaBussiness():
    return lista()
