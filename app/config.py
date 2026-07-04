import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

MAX_CONTENT_LENGTH = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "pdf"
}
