# Archivo de configuracion del servidor 

KEY = b'\xc2bAA\xc4-\xdd!\xac\x08\x1a\xde\xa2xeW'

class BaseConfig(object): #  Configuraciones basicas del servidor 
	SECRET_KEY = KEY
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/freedbm_data'
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductConfig(BaseConfig): # Configuraciones para el modo de producción
	DEBUG = False

class DevelopmentConfig(BaseConfig): # Configuraciones para el modo de desarrollo
	DEBUG = True