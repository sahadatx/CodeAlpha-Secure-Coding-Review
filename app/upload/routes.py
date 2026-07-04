from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    request
)

from decorators import login_required

# Create Blueprint
upload_bp = Blueprint("upload", __name__)


# ======================================================
# Upload
# ======================================================
@upload_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    filename = None

    if request.method == "POST":

        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename:

            upload_dir = (
                Path(__file__).resolve().parent.parent
                / "uploads"
            )

            upload_dir.mkdir(exist_ok=True)

            save_path = upload_dir / uploaded_file.filename

            # ------------------------------------------------
            # INTENTIONALLY WEAK
            # Missing file validation
            # ------------------------------------------------
            uploaded_file.save(save_path)

            filename = uploaded_file.filename

    return render_template(
        "upload.html",
        filename=filename
    )
