from flask import Flask
import config

from auth.routes import auth_bp
from main.routes import main_bp
from search.routes import search_bp
from profile.routes import profile_bp
from upload.routes import upload_bp
from admin.routes import admin_bp

app = Flask(__name__)

# Load all UPPERCASE variables from config.py
app.config.from_object(config)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(search_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=config.DEBUG)
