Implementación de un ejemplo de CRUD en capas (MVC)

Integrantes
Juan Camilo Herrera
Cristian Camilo Roncancio

Se utilizo el framework flask y sqlite3 para la persistencia de los datos
Para la instalación y ejecución del proyecto instalar los siguiente componentes:

flask
SQLAlchemy

para la ejecución del proyecto usar el siguiente comando:

py app.py

Distribución del proyecto:
1. En la carpeta Templates: Se encuentra la vista es un archivo html que contiene un formulario de datos basicos.
2. En la carpeta Model se encontrara todo lo relacionado con la lógica de negocio del formulario
3. En la carpeta Controller se encuentra la interacción con la base de datos (Update,Delete,Insert y retorno de listas).

4. En la carpeta Database se encuentra un archivo de sqlite donde se registra la información recibida a través del formulario

