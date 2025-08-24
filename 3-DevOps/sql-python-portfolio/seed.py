from faker import Faker
from werkzeug.security import generate_password_hash
from app import app
from extensions import db
from models import User, Post

fake = Faker()

with app.app_context():
    # Optional: clear existing demo data (careful in production)
    db.session.query(Post).delete()
    db.session.query(User).delete()
    db.session.commit()

    users = []
    for i in range(3):
        u = User(
            username=f"user{i+1}",
            email=f"user{i+1}@example.com",
            password_hash=generate_password_hash("password123"),
        )
        db.session.add(u)
        users.append(u)
    db.session.commit()

    for u in users:
        for _ in range(3):
            p = Post(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=3),
                user_id=u.id
            )
            db.session.add(p)
    db.session.commit()
    print("Seeded users and posts.")
