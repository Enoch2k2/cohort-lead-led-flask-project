from config import db


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    def __repr__(self):
        return f'<Song id={self.id} name={self.name}>'
