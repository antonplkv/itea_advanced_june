import mongoengine as me
import datetime

me.connect('schema_lesson13')

class Post(me.Document):
    title = me.StringField(min_length=2, max_length=1024)
    body = me.StringField(min_length=2, max_length=4096)
    created = me.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.id)


class Author(me.Document):
    login = me.StringField(unique=True, min_length=6, max_length=255)
    password = me.StringField(min_length=8, max_length=512)
    post = me.ReferenceField(Post)