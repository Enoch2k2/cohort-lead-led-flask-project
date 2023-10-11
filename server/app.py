# setup our python server here
from config import app


if (__name__ == "__main__"):
    app.run(port=8000, debug=True)
