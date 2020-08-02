from app import *
import os

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api
from dotenv import load_dotenv


load_dotenv()

app = create_app(os.getenv('ENV'))

CORS(app)

jwt = JWTManager(app)

api = Api(app,version='1.0', doc='/api/v1/documentation', license="MIT", title="JBR Health Service", description="Digital Health Service Backend API")
api = api.namespace('/api/v1', description='<b style="font-size: 20px">End Points Definition</b>')