import mongoengine as me

me.connect('rest_test_api')


class User(me.Document):
    login = me.StringField(min_length=2, max_length=255, required=True, unique=True)
    password = me.StringField(min_length=8, max_length=256, required=True)
    confirmed_password = me.StringField(min_length=8, max_length=256, required=True)