from config import app, db
from models.models import *

with app.app_context():
    print("Deleting data...")
    Genre.query.delete()
    db.session.commit()

    print('Generating Genres...')

    genre_1 = Genre(name="Pop")
    genre_2 = Genre(name="Rock")
    genre_3 = Genre(name="Rap")

    db.session.add_all([genre_1, genre_2, genre_3])
    db.session.commit()

    print("Seeding completed...")
