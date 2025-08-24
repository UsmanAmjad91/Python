from flask import Blueprint, request, jsonify, abort
from sqlalchemy import or_
from extensions import db
from models import User, Profile, Post

api_bp = Blueprint("api", __name__)

# ------------- Helpers -------------
def paginate(query):
    page = max(int(request.args.get("page", 1)), 1)
    per_page = min(max(int(request.args.get("per_page", 20)), 1), 100)
    items = query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        "items": items.items,
        "meta": {
            "page": items.page,
            "per_page": items.per_page,
            "total": items.total,
            "pages": items.pages,
        },
    }

@api_bp.app_errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@api_bp.app_errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

# ------------- Users -------------
@api_bp.get("/users")
def list_users():
    q = User.query.order_by(User.id.desc())
    data = paginate(q)
    return jsonify({
        "data": [u.to_dict() for u in data["items"]],
        "meta": data["meta"]
    })

@api_bp.post("/users")
def create_user():
    payload = request.get_json(force=True, silent=True) or {}
    username = payload.get("username")
    email = payload.get("email")
    bio = payload.get("bio", "")
    if not username or not email:
        abort(400)
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "username or email already exists"}), 409
    u = User(username=username, email=email)
    db.session.add(u)
    db.session.flush()  # get id
    if bio:
        p = Profile(user_id=u.id, bio=bio)
        db.session.add(p)
    db.session.commit()
    return jsonify(u.to_dict()), 201

@api_bp.get("/users/<int:user_id>")
def get_user(user_id):
    u = User.query.get_or_404(user_id)
    return jsonify(u.to_dict())

@api_bp.put("/users/<int:user_id>")
def update_user(user_id):
    u = User.query.get_or_404(user_id)
    payload = request.get_json(force=True, silent=True) or {}
    username = payload.get("username")
    email = payload.get("email")
    bio = payload.get("bio")

    if username:
        u.username = username
    if email:
        u.email = email
    if bio is not None:
        if u.profile is None:
            from models import Profile
            u.profile = Profile(bio=bio, user=u)
        else:
            u.profile.bio = bio
    db.session.commit()
    return jsonify(u.to_dict())

@api_bp.delete("/users/<int:user_id>")
def delete_user(user_id):
    u = User.query.get_or_404(user_id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({"status": "deleted"})

# ------------- Posts -------------
@api_bp.get("/posts")
def list_posts():
    topic = request.args.get("topic")
    qstr = request.args.get("q")
    q = Post.query
    if topic:
        q = q.filter(Post.topic == topic)
    if qstr:
        q = q.filter(or_(Post.content.ilike(f"%{qstr}%"), Post.topic.ilike(f"%{qstr}%")))
    q = q.order_by(Post.created_at.desc())

    data = paginate(q)
    return jsonify({
        "data": [p.to_dict() for p in data["items"]],
        "meta": data["meta"]
    })

@api_bp.post("/posts")
def create_post():
    payload = request.get_json(force=True, silent=True) or {}
    author_id = payload.get("author_id")
    topic = payload.get("topic")
    content = payload.get("content")
    if not all([author_id, topic, content]):
        abort(400)
    if User.query.get(author_id) is None:
        return jsonify({"error": "author_id not found"}), 404
    p = Post(author_id=author_id, topic=topic, content=content)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict()), 201

@api_bp.get("/posts/<int:post_id>")
def get_post(post_id):
    p = Post.query.get_or_404(post_id)
    return jsonify(p.to_dict())

@api_bp.put("/posts/<int:post_id>")
def update_post(post_id):
    p = Post.query.get_or_404(post_id)
    payload = request.get_json(force=True, silent=True) or {}
    topic = payload.get("topic")
    content = payload.get("content")
    if topic:
        p.topic = topic
    if content:
        p.content = content
    db.session.commit()
    return jsonify(p.to_dict())

@api_bp.delete("/posts/<int:post_id>")
def delete_post(post_id):
    p = Post.query.get_or_404(post_id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"status": "deleted"})

# ------------- Likes -------------
@api_bp.post("/posts/<int:post_id>/like")
def like_post(post_id):
    payload = request.get_json(force=True, silent=True) or {}
    user_id = payload.get("user_id")
    if not user_id:
        abort(400)
    p = Post.query.get_or_404(post_id)
    u = User.query.get_or_404(user_id)
    if p.liked_by.filter_by(id=u.id).first() is None:
        p.liked_by.append(u)
        db.session.commit()
    return jsonify(p.to_dict())

@api_bp.post("/posts/<int:post_id>/unlike")
def unlike_post(post_id):
    payload = request.get_json(force=True, silent=True) or {}
    user_id = payload.get("user_id")
    if not user_id:
        abort(400)
    p = Post.query.get_or_404(post_id)
    u = User.query.get_or_404(user_id)
    if p.liked_by.filter_by(id=u.id).first() is not None:
        p.liked_by.remove(u)
        db.session.commit()
    return jsonify(p.to_dict())

# ------------- Stats -------------
@api_bp.get("/stats/posts-by-topic")
def posts_by_topic():
    from sqlalchemy import func
    rows = (
        db.session.query(Post.topic, func.count(Post.id).label("count"))
        .group_by(Post.topic)
        .order_by(func.count(Post.id).desc())
        .all()
    )
    data = [{"topic": r[0], "count": int(r[1])} for r in rows]
    return jsonify({"data": data})
