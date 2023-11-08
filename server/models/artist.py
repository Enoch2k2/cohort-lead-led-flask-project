from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    songs = db.relationship("Song", back_populates="artist")
    genres = db.relationship(
        "Genre", secondary="songs", back_populates="artists")

    serialize_rules = (
        "-songs.artist",
        "-songs.genre",
        "-genres.artists",
        "-genres.songs",
    )

    @validates("name")
    def validate_name(self, attr, name):
        if len(name) == 0:
            raise ValueError("name can't be blank")

        return name

    def __repr__(self):
        return f'<Artist id={self.id} name={self.name}>'
