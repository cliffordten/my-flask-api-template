from flask import request
from datetime import date, datetime
from flask_restx import Resource, reqparse

from models.hello import HelloModel
from utils.response import *

from resources import setDocumentaiondb


class Hello(Resource):

    def get(self):

        HelloModel.bind = setDocumentaiondb(request)

        if(HelloModel.bind):
            print('passed')

        data = HelloModel("Boiler Plate Production Sever Running")

        data .save_to_db()
        
        return success(data.json())