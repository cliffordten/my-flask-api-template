from flask import request
from datetime import date, datetime
from flask_restx import Resource, reqparse
from app.app import app
from dotenv import load_dotenv

from models.hello import HelloModel
from utils.response import *


class Hello(Resource):

    def get(self):

        data = HelloModel("Boiler Plate Production Sever Running")

        data.save_to_db()

        return success(data.json())
