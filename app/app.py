from flask import Flask

from config import SECRET_KEY, DEBUG

from auth import register

from routes import routes

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY


register(app)

routes(app)


if __name__ == "__main__":

    app.run(debug=DEBUG)
