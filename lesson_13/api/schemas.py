from marshmallow import Schema, fields


class Post(Schema):
    id = fields.String()
    title = fields.String()
    body = fields.String()
    created = fields.DateTime()


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    login = fields.String()
    password = fields.String(load_only=True)
    post = fields.Nested(Post)

    
class AuthorCreateSchema(AuthorSchema):
    post = fields.String()