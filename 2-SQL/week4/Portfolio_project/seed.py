import random
from faker import Faker

from app import app
from extensions import db
from models import User, Profile, Post

fake = Faker()

def seed():
    with app.app_context():
        # Clear existing
        Post.query.delete()
        Profile.query.delete()
        User.query.delete()
        db.session.commit()

        # Users + profiles
        users = []
        for i in range(10):
            u = User(username=f"user{i+1}", email=f"user{i+1}@example.com")
            db.session.add(u)
            db.session.flush()
            p = Profile(user_id=u.id, bio=fake.sentence(nb_words=10))
            db.session.add(p)
            users.append(u)
        db.session.commit()

        topics = ["python", "flask", "sql", "postgres", "visualization"]
        # Posts
        posts = []
        for _ in range(40):
            author = random.choice(users)
            topic = random.choice(topics)
            content = fake.paragraph(nb_sentences=3)
            posts.append(Post(author_id=author.id, topic=topic, content=content))
        db.session.add_all(posts)
        db.session.commit()

        # Likes
        for p in posts:
            for u in random.sample(users, k=random.randint(0, len(users)//2)):
                p.liked_by.append(u)
        db.session.commit()

        print("Seeded! users:", len(users), "posts:", len(posts))

if __name__ == "__main__":
    seed()
