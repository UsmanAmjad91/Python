import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from config import get_config
from extensions import db, migrate
from routes import api_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    app.register_blueprint(api_bp)

    # Base URL message
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "status": "ok",
            "message": "App connected. See /api/ for endpoints."
        })

    # JSON error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Server error"}), 500

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
