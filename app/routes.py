from flask import render_template, session, request

from decorators import login_required
from database import get_connection


def routes(app):

    # ----------------------------
    # Home
    # ----------------------------
    @app.route("/")
    def home():

        return render_template("index.html")


    # ----------------------------
    # Dashboard
    # ----------------------------
    @app.route("/dashboard")
    @login_required
    def dashboard():

        return render_template(
            "dashboard.html",
            username=session["username"]
        )


    # ----------------------------
    # Search (Intentionally Vulnerable)
    # ----------------------------
    @app.route("/search", methods=["GET", "POST"])
    @login_required
    def search():

        results = []

        if request.method == "POST":

            keyword = request.form["search"]

            conn = get_connection()
            cursor = conn.cursor()

            # ----------------------------------------
            # INTENTIONALLY VULNERABLE
            # SQL Injection (For Learning Purpose)
            # ----------------------------------------
            query = (
                f"SELECT * FROM users "
                f"WHERE username LIKE '%{keyword}%'"
            )

            cursor.execute(query)

            results = cursor.fetchall()

            conn.close()

        return render_template(
            "search.html",
            results=results
        )
