from flask import (
    Blueprint,
    render_template,
    request
)

from decorators import login_required
from database import get_connection

search_bp = Blueprint("search", __name__)


@search_bp.route("/search", methods=["GET", "POST"])
@login_required
def search():

    results = []

    if request.method == "POST":

        keyword = request.form["search"]

        conn = get_connection()
        cursor = conn.cursor()

        # ------------------------------------------
        # Secure Query (SQL Injection Prevented)
        # ------------------------------------------
        cursor.execute(
            "SELECT * FROM users WHERE username LIKE ?",
            ("%" + keyword + "%",)
        )

        results = cursor.fetchall()

        conn.close()

    return render_template(
        "search.html",
        results=results
    )
