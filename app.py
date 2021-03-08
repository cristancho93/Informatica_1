from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from Model.personBusiness import *

app = Flask(__name__)
#Conexión a la base de datos sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database/Informatica1.db'
db = SQLAlchemy(app)

from Data.person import personForm

#Ruta por defecto de arranque de la app
@app.route('/')
def home():
    persons = listaBussiness()
    return render_template('Index.html', persons = persons)

@app.route('/create-person', methods=['POST'])
def save():
    person = personForm(nombre=request.form['nombre'], apellido=request.form['apellido'], telefono=request.form['telefono'])
    return saveItem(person)

@app.route('/delete-person/<id>')
def delete(id):
    return deleteItem(id)

@app.route('/update-person', methods=['POST'])
def update():
    person = personForm(id=request.form['id'], nombre=request.form['nombre'], apellido=request.form['apellido'], telefono=request.form['telefono'])
    return updateItem(person)

if(__name__ == '__main__'):
    app.run(debug=True)
