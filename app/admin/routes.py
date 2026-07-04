from flask import (
    Blueprint,
    render_template,
    session
)

from decorators import login_required

# Create Blueprint
admin_bp = Blueprint("admin", __name__)


# ======================================================
# Admin Panel
# ======================================================
@admin_bp.route("/admin")
@login_required
def admin():

    # ------------------------------------------------
    # INTENTIONALLY VULNERABLE
    # No Authorization Check
    # ------------------------------------------------

    return render_template(
        "admin.html",
        username=session["username"]
    )
