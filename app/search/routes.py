from flask import (
    Blueprint,
    render_template,
    request
)

from decorators import login_required
from database import get_connection

# Create Blueprint
search_bp = Blueprint("search", __name__)


# ======================================================
# Search Users
# ======================================================
@search_bp.route("/search", methods=["GET", "POST"])
@login_required
def search():

    results = []

    if request.method == "POST":

        keyword = request.form.get("search", "")

        conn = get_connection()
        cursor = conn.cursor()

        # ------------------------------------------------
        # INTENTIONALLY VULNERABLE
        # SQL Injection (For Secure Coding Review)
        # ------------------------------------------------
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
