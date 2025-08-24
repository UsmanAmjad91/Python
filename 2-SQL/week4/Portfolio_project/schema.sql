-- Raw SQL schema equivalent (for reference or quick setup)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    bio TEXT DEFAULT '',
    user_id INTEGER NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(80) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS likes (
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    CONSTRAINT uq_like_user_post UNIQUE (user_id, post_id),
    PRIMARY KEY (user_id, post_id)
);

-- Performance indexes
CREATE INDEX IF NOT EXISTS ix_users_username ON users (username);
CREATE INDEX IF NOT EXISTS ix_users_email ON users (email);
CREATE INDEX IF NOT EXISTS ix_posts_topic ON posts (topic);
CREATE INDEX IF NOT EXISTS ix_posts_created_at ON posts (created_at);
CREATE INDEX IF NOT EXISTS ix_posts_author_id ON posts (author_id);
CREATE INDEX IF NOT EXISTS ix_posts_topic_created ON posts (topic, created_at);
