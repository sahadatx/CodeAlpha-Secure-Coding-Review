from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash
)

from database import get_connection
from decorators import login_required

# Create Blueprint
auth_bp = Blueprint("auth", __name__)


# ======================================================
# Register
# ======================================================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        # ------------------------------------------------
        # INTENTIONALLY INSECURE
        # Plain Text Password Storage
        # ------------------------------------------------
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        flash("Registration Successful. Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ======================================================
# Login
# ======================================================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # ------------------------------------------------
        # INTENTIONALLY VULNERABLE
        # SQL Injection (For Learning Purpose)
        # ------------------------------------------------
        query = (
            f"SELECT * FROM users "
            f"WHERE username='{username}' "
            f"AND password='{password}'"
        )

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(query)

        user = cursor.fetchone()

        conn.close()

        if user:

            session["username"] = username

            flash("Login Successful!", "success")

            return redirect(url_for("main.dashboard"))

        flash("Invalid Username or Password.", "danger")

    return render_template("login.html")


# ======================================================
# Logout
# ======================================================
@auth_bp.route("/logout")
@login_required
def logout():

    session.clear()

    flash("Logged Out Successfully.", "success")

    return redirect(url_for("auth.login"))
