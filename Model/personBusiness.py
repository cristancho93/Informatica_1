from Controller.personDll import *
from flask import request
from app import *


def validate(person):
    print("Entro Bussiness")
    person = personForm(content=request.form['nombre', 'apellido', 'telefono']);
    create(person);
