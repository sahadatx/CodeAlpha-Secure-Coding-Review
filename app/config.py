import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "CodeAlpha-Secure-Coding-Review"

DEBUG = True

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "pdf"
}
