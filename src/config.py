# Archivo de configuracion del servidor 

class BaseConfig(object): #  Configuraciones basicas del servidor 
	SECRET_KEY = b'\xc2bAA\xc4-\xdd!\xac\x08\x1a\xde\xa2xeW'
	# SQLALCHEMY_DATABASE_URI = 
	# SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductConfig(BaseConfig): # Configuraciones para el modo de producción
	DEBUG = False

class DevelopmentConfig(BaseConfig): # Configuraciones para el modo de desarrollo
	DEBUG = True