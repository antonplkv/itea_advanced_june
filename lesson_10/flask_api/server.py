from flask import Flask, request, jsonify
from models import User

import json

app = Flask(__name__)


@app.route('/users', methods=['GET', 'POST'])
def get_user():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':

        #user = User.objects.create(login='mylogin', password='password', confirmed_password='password')
        user = User.objects.create(**request.json)
        serialized_user = json.dumps({'id': str(user.id), 'login': user.login})

        # return app.response_class(
        #     response=serialized_user,
        #     status=201,
        #     mimetype='application/json'
        # )
        return jsonify({'id': str(user.id), 'login': user.login})




app.run(debug=True)
