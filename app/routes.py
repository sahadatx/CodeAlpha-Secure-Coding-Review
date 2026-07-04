from flask import render_template, session

from decorators import login_required


def routes(app):

    @app.route("/")
    def home():

        return render_template("index.html")


    @app.route("/dashboard")
    @login_required
    def dashboard():

        return render_template(
            "dashboard.html",
            username=session["username"]
        )
