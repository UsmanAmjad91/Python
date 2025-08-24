from datetime import datetime
from extensions import db

likes = db.Table(
    "likes",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.UniqueConstraint("user_id", "post_id", name="uq_like_user_post"),
)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    profile = db.relationship("Profile", uselist=False, back_populates="user", cascade="all, delete-orphan")
    posts = db.relationship("Post", back_populates="author", cascade="all, delete-orphan")
    liked_posts = db.relationship("Post", secondary=likes, back_populates="liked_by", lazy="dynamic")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "bio": self.profile.bio if self.profile else "",
        }

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text, default="")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    user = db.relationship("User", back_populates="profile")

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True, nullable=False)
    author = db.relationship("User", back_populates="posts")

    liked_by = db.relationship("User", secondary=likes, back_populates="liked_posts", lazy="dynamic")

    __table_args__ = (
        db.Index("ix_posts_topic_created", "topic", "created_at"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "author_id": self.author_id,
            "likes": self.liked_by.count() if hasattr(self.liked_by, "count") else 0,
        }
