from flask import (
    Blueprint,
    render_template,
    session
)

from decorators import login_required
from database import get_connection

# Create Blueprint
profile_bp = Blueprint("profile", __name__)


# ======================================================
# Profile
# ======================================================
@profile_bp.route("/profile")
@login_required
def profile():

    conn = get_connection()
    cursor = conn.cursor()

    # ------------------------------------------------
    # INTENTIONALLY VULNERABLE
    # Information Disclosure
    # ------------------------------------------------
    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (session["username"],)
    )

    user = cursor.fetchone()

    conn.close()

    return render_template(
        "profile.html",
        user=user
    )
