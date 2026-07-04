from flask import (
    Blueprint,
    render_template,
    session
)

from decorators import login_required

# Create Blueprint
main_bp = Blueprint("main", __name__)


# ======================================================
# Home
# ======================================================
@main_bp.route("/")
def home():

    return render_template("index.html")


# ======================================================
# Dashboard
# ======================================================
@main_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        username=session["username"]
    )
