from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "username" not in session:

            flash("Please login first.", "warning")

            return redirect(url_for("login"))

        return func(*args, **kwargs)

    return wrapper
