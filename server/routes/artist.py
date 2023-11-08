from flask import request
from flask_restful import Resource
from models.models import Artist
from config import api, db
from sqlalchemy.exc import IntegrityError


class ArtistsResource(Resource):
    def get(self):
        artists = [artist.to_dict() for artist in Artist.query.all()]
        return artists, 200

    def post(self):
        data = request.get_json()
        name = data["name"]
        # hasattr / getattr / setattr like the send method in ruby
        try:
            artist = Artist(name=name)
            db.session.add(artist)
            db.session.commit()
            return artist.to_dict(), 201
        except IntegrityError:
            return {"error": "Name has already been taken"}, 422
        except ValueError as err:
            return {"error": str(err)}, 422


api.add_resource(ArtistsResource, "/api/artists")
