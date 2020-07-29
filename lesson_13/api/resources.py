from flask_restful import Resource
from .schemas import AuthorSchema
from .models import Author


class AuthorResource(Resource):

    def get(self, author_id=None):
        if author_id:
            return AuthorSchema().dump(Author.objects.get(id=author_id), many=True)

        return AuthorSchema().dump(Author.objects, many=True)
