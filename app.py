from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from Model.personBusiness import *

app = Flask(__name__)
#Conexión a la base de datos sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database/Informatica1.db'
db = SQLAlchemy(app)

#Ruta por defecto de arranque del formulario
@app.route('/')
def home():
    return render_template('Index.html')

class personForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    telefono = db.Column(db.String(10))

@app.route('/create-person', methods=['POST'])
def save():
    print("app save")
    person = personForm(request.form['nombre', 'apellido', 'telefono'])
    print(person + "Impresion persona")
    #validate(person)

if(__name__ == '__main__'):
    app.run(debug=True)
