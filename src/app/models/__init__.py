from flask_sqlalchemy import SQLAlchemy
from app import app 
import datetime

db = SQLAlchemy(app) # Inicializa un objeto SQLAlchemy

from .users import *
from .movies import *