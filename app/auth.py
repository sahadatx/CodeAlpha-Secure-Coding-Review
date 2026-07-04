from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash
)

from decorators import login_required
from database import get_connection


def register(app):

    @app.route("/register", methods=["GET", "POST"])
    def register_route():

        if request.method == "POST":

            username = request.form["username"]
            password = request.form["password"]

            conn = get_connection()

            cursor = conn.cursor()

            # Intentionally insecure
            cursor.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, password)
            )

            conn.commit()

            conn.close()

            flash("Registration Successful", "success")

            return redirect(url_for("login"))

        return render_template("register.html")


    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":

            username = request.form["username"]
            password = request.form["password"]

            # Intentionally Vulnerable
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

            conn = get_connection()

            cursor = conn.cursor()

            cursor.execute(query)

            user = cursor.fetchone()

            conn.close()

            if user:

                session["username"] = username

                flash("Login Successful", "success")

                return redirect(url_for("dashboard"))

            flash("Invalid Credentials", "danger")

        return render_template("login.html")


    @app.route("/logout")
    @login_required
    def logout():

        session.clear()

        flash("Logged Out Successfully", "success")

        return redirect(url_for("login"))
