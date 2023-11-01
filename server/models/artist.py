from config import db


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    songs = db.relationship("Song", back_populates="artist")
    genres = db.relationship(
        "Genre", secondary="songs", back_populates="artists")

    def __repr__(self):
        return f'<Artist id={self.id} name={self.name}>'
