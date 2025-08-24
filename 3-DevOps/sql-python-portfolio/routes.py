from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Post, Like
from functools import wraps

api_bp = Blueprint("api", __name__, url_prefix="/api")

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Authentication required"}), 401
        return fn(*args, **kwargs)
    return wrapper

def owner_required(resource_user_id):
    if resource_user_id != session.get("user_id"):
        return jsonify({"error": "Forbidden"}), 403
    return None

@api_bp.route("/", methods=["GET"])
def api_root():
    return jsonify({
        "message": "API connected",
        "endpoints": [
            "POST   /api/auth/register",
            "POST   /api/auth/login",
            "POST   /api/auth/logout",
            "GET    /api/auth/me",
            "GET    /api/users",
            "GET    /api/users/<id>",
            "PUT    /api/users/<id>",
            "DELETE /api/users/<id>",
            "POST   /api/posts",
            "GET    /api/posts?user_id=<id>",
            "GET    /api/posts/<id>",
            "PUT    /api/posts/<id>",
            "DELETE /api/posts/<id>",
            "POST   /api/posts/<id>/like",
            "POST   /api/posts/<id>/unlike",
            "GET    /api/posts/<id>/likes"
        ]
    })

@api_bp.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json(force=True, silent=True) or {}
    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "username, email, password are required"}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password),
    )
    db.session.add(user)
    db.session.commit()
    session["user_id"] = user.id
    return jsonify({"message": "Registered", "user": user.to_dict()}), 201

@api_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json(force=True, silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        session["user_id"] = user.id
        return jsonify({"message": "Login successful", "user": user.to_dict()})
    return jsonify({"error": "Invalid credentials"}), 401

@api_bp.route("/auth/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})

@api_bp.route("/auth/me", methods=["GET"])
@login_required
def me():
    user = User.query.get_or_404(session["user_id"])
    return jsonify(user.to_dict())

@api_bp.route("/users", methods=["GET"])
def list_users():
    users = User.query.order_by(User.id.asc()).all()
    return jsonify([u.to_dict() for u in users])

@api_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    u = User.query.get_or_404(user_id)
    return jsonify(u.to_dict())

@api_bp.route("/users/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    perm = owner_required(user.id)
    if perm:
        return perm

    data = request.get_json(force=True, silent=True) or {}
    if "username" in data:
        user.username = (data["username"] or "").strip()
    if "email" in data:
        user.email = (data["email"] or "").strip().lower()
    if "password" in data and data["password"]:
        user.password_hash = generate_password_hash(data["password"])

    db.session.commit()
    return jsonify(user.to_dict())

@api_bp.route("/users/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    perm = owner_required(user.id)
    if perm:
        return perm

    db.session.delete(user)
    db.session.commit()
    session.clear()
    return jsonify({"message": "User deleted"})

@api_bp.route("/posts", methods=["POST"])
@login_required
def create_post():
    data = request.get_json(force=True, silent=True) or {}
    title = (data.get("title") or "").strip()
    content = (data.get("content") or "").strip()

    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400

    post = Post(title=title, content=content, user_id=session["user_id"])
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@api_bp.route("/posts", methods=["GET"])
def list_posts():
    user_id = request.args.get("user_id", type=int)
    q = Post.query
    if user_id:
        q = q.filter(Post.user_id == user_id)
    posts = q.order_by(Post.id.desc()).all()
    return jsonify([p.to_dict() for p in posts])

@api_bp.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())

@api_bp.route("/posts/<int:post_id>", methods=["PUT"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    perm = owner_required(post.user_id)
    if perm:
        return perm

    data = request.get_json(force=True, silent=True) or {}
    if "title" in data and data["title"] is not None:
        post.title = data["title"].strip()
    if "content" in data and data["content"] is not None:
        post.content = data["content"].strip()
    db.session.commit()
    return jsonify(post.to_dict())

@api_bp.route("/posts/<int:post_id>", methods=["DELETE"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    perm = owner_required(post.user_id)
    if perm:
        return perm
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"})

@api_bp.route("/posts/<int:post_id>/like", methods=["POST"])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    existing = Like.query.filter_by(post_id=post.id, user_id=session["user_id"]).first()
    if existing:
        return jsonify({"error": "Already liked"}), 400
    like = Like(post_id=post.id, user_id=session["user_id"])
    db.session.add(like)
    db.session.commit()
    return jsonify({"message": "Post liked", "likes_count": len(post.likes)}), 201

@api_bp.route("/posts/<int:post_id>/unlike", methods=["POST"])
@login_required
def unlike_post(post_id):
    post = Post.query.get_or_404(post_id)
    existing = Like.query.filter_by(post_id=post.id, user_id=session["user_id"]).first()
    if not existing:
        return jsonify({"error": "Not liked yet"}), 400
    db.session.delete(existing)
    db.session.commit()
    return jsonify({"message": "Post unliked", "likes_count": len(post.likes)})

@api_bp.route("/posts/<int:post_id>/likes", methods=["GET"])
def list_likes(post_id):
    post = Post.query.get_or_404(post_id)
    user_ids = [like.user_id for like in post.likes]
    return jsonify({"post_id": post.id, "likes_count": len(user_ids), "user_ids": user_ids})
