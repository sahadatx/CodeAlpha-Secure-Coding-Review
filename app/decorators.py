from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash
)


# ======================================================
# Login Required
# ======================================================
def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "username" not in session:

            flash(
                "Please login first.",
                "warning"
            )

            return redirect(
                url_for("auth.login")
            )

        return func(*args, **kwargs)

    return wrapper


# ======================================================
# Admin Required
# ======================================================
def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # User is not logged in
        if "username" not in session:

            flash(
                "Please login first.",
                "warning"
            )

            return redirect(
                url_for("auth.login")
            )

        # User is logged in but not an admin
        if session.get("role") != "admin":

            flash(
                "Access denied. Admin only.",
                "danger"
            )

            return redirect(
                url_for("main.dashboard")
            )

        return func(*args, **kwargs)

    return wrapper
