from Controller.personController import *
from flask import request
from app import *


def saveItem(person):
    validation = False
    if person.nombre and person.apellido and person.telefono:
        validation = True
    else:
        validation = False

    if validation:
        create(person)
    else:
        return "Revise que los campos del formulario esten diligenciados"

def listaBussiness ():
    return lista()


