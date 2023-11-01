from config import db


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))

    artist = db.relationship("Artist", back_populates="songs")
    genre = db.relationship("Genre", back_populates="songs")

    def __repr__(self):
        return f'<Song id={self.id} name={self.title}>'
