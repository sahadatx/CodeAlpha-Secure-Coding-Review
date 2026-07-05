from flask import (
    Blueprint,
    render_template,
    session
)

from decorators import (
    login_required,
    admin_required
)

# Create Blueprint
admin_bp = Blueprint("admin", __name__)


# ======================================================
# Admin Panel
# ======================================================
@admin_bp.route("/admin")
@login_required
@admin_required
def admin():

    return render_template(
        "admin.html",
        username=session["username"],
        role=session["role"]
    )