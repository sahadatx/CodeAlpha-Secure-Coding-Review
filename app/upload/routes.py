from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    current_app
)

from werkzeug.utils import secure_filename

from decorators import login_required

# Create Blueprint
upload_bp = Blueprint("upload", __name__)


# ======================================================
# Allowed File Types
# ======================================================
def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


# ======================================================
# Upload
# ======================================================
@upload_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    filename = None

    if request.method == "POST":

        uploaded_file = request.files.get("file")

        # No file selected
        if uploaded_file is None:

            flash("No file selected.", "danger")

            return render_template(
                "upload.html",
                filename=filename
            )

        # Empty filename
        if uploaded_file.filename == "":

            flash("Please choose a file.", "warning")

            return render_template(
                "upload.html",
                filename=filename
            )

        # Validate extension
        if not allowed_file(uploaded_file.filename):

            flash("Invalid file type. Only PNG, JPG, JPEG and PDF are allowed.", "danger")

            return render_template(
                "upload.html",
                filename=filename
            )

        # Secure filename
        filename = secure_filename(uploaded_file.filename)

        upload_dir = Path(
            current_app.config["UPLOAD_FOLDER"]
        )

        upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        save_path = upload_dir / filename

        uploaded_file.save(save_path)

        flash("File uploaded successfully.", "success")

    return render_template(
        "upload.html",
        filename=filename
    )
