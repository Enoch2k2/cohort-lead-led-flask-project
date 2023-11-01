from flask_restful import Resource
from config import api


class ArtistsResource(Resource):
    def get(self):
        return {"message": "This works!"}, 200


api.add_resource(ArtistsResource, "/api/artists")
