from flask import Flask 
from flask_restful import Api
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig) 
api = Api(app)

