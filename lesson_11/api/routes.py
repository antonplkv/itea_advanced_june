from flask import Flask
from flask_restful import Api
from .resources import VehicleResource, ManufacturerResource

app = Flask(__name__)
api = Api(app)

api.add_resource(VehicleResource, '/vehicles', '/vehicles/<vehicle_id>')
api.add_resource(ManufacturerResource, '/manufacturers', '/manufacturers/<manufacturer_id>')