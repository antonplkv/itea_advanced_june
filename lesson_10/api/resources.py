from flask_restful import Resource
from flask import request
import json

from .models import User


class UserResource(Resource):

    def get(self, user_id=None):

        if user_id is None:
            return json.loads(User.objects().to_json())
        else:
            return json.loads(User.objects(id=user_id))

    def post(self):
        user = User.objects.create(**request.json)
        return json.loads(user.to_json())

    def put(self):
        print('put')

    def delete(self, user_id):
        User.objects(id=user_id).delete()