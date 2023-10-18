# setup our python server here
from config import app
from models.models import *

if (__name__ == "__main__"):
    app.run(port=8000, debug=True)
