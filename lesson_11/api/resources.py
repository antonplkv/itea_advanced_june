from flask_restful import Resource
from flask import request
from .models import Vehicle, Manufacturer
from .schemas import VehicleSchema
from marshmallow import ValidationError


class VehicleResource(Resource):

    def get(self, vehicle_id=None):
        queryset = Vehicle.objects
        if vehicle_id:
            return VehicleSchema().dump(queryset.get(id=vehicle_id))
        else:
            return VehicleSchema().dump(queryset, many=True)

    def post(self):
        try:
            res = VehicleSchema().load(request.get_json())
            obj = Vehicle.objects.create(**res)
            return VehicleSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, vehicle_id):
        try:
            res = VehicleSchema().load(request.get_json())
            obj = Vehicle.objects.get(id=vehicle_id)
            res['manufacturer'] = Manufacturer.objects.get(id=res['manufacturer'])
            obj.update(**res)
            return VehicleSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, vehicle_id):
        Vehicle.objects(id=vehicle_id).delete()
        return {'status': 'deleted'}


class ManufacturerResource(Resource):

    def get(self, manufacturer_id=None):
        pass

    def post(self):
        pass

    def put(self, manufacturer_id):
        pass

    def delete(self, manufacturer_id):
        pass