from flask import Flask, render_template, request
import sqlite3
from config import SECRET_KEY, DEBUG

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

DATABASE = "database.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        # Intentionally insecure (Plain Text Password)
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return "Registration Successful"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Intentionally vulnerable (SQL Injection)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(query)

        user = cursor.fetchone()

        conn.close()

        if user:
            return "Login Successful"

        return "Invalid Username or Password"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=DEBUG)