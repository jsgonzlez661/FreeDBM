from flask import Flask 
from flask_restful import Api
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig) 
api = Api(app)

from app.resource.signup import Signup
from app.resource.login import Login
from app.resource.logout import Logout

api.add_resource(Signup, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
api.add_resource(Logout, '/api/v1/auth/logout')

