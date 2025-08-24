from flask import Flask
from config import Config
from extensions import db, migrate
from routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.get("/")
    def root():
        return {"status": "ok", "message": "SQL+Python Portfolio API"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run()
