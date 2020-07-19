from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from app import api
from app.models import db
from app.models import User
from sqlalchemy.sql import select
import bcrypt
import jwt
import config




