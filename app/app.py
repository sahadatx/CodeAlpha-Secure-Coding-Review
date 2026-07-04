from flask import Flask, render_template
from config import SECRET_KEY, DEBUG

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def home():

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=DEBUG)