# Archivo que inicia la aplicacion 

from app import app # Importa las configuraciones del archivo __init__.py de la carpeta app
from app.models import db  # Importa la clase db de la carpeta app\models


if __name__ == '__main__':
	db.init_app(app) # Inicia la base de datos
	with app.app_context():  # Crea las tablas en la base de datos si no existe
		db.create_all()
	app.run()   # Inicia el servidor 