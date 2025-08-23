# SQL with Python Portfolio Project

This repository contains a complete, minimal starter for your Week 4 Portfolio Project:
- PostgreSQL schema and ER relationships (1–1, 1–many, many–many)
- Flask REST API (CRUD) with SQLAlchemy and Flask-Migrate
- Insomnia collection (GET/POST/PUT/DELETE ready)
- Performance enhancements (non-PK index)
- Optional Google Colab visualization snippet
- Step-by-step commands to run everything locally with or without Docker

---

## 1) Prerequisites

- Python 3.10+
- PostgreSQL 14+ (local or Docker)
- `pip` and `virtualenv` (optional but recommended)

### Option A — Run Postgres via Docker
```bash
docker compose -f docker-compose.yml up -d
# Postgres will be on localhost:5432 (user: postgres / password: postgres)
```

### Option B — Local Postgres
Create a database named `portfolio_db` (or any name you like):
```sql
CREATE DATABASE portfolio_db;
```

---

## 2) Configure environment

Copy `.env.example` → `.env` and adjust if needed.
```bash
cp .env.example .env
```

Key variables:
- `DATABASE_URL` e.g. `postgresql+psycopg2://postgres:postgres@localhost:5432/portfolio_db`
- `FLASK_APP=app.py`

---

## 3) Install & run the API

```bash
# from the project root
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Initialize DB (using Flask-Migrate)
flask db init
flask db migrate -m "initial schema"
flask db upgrade

# (Optional) Add performance indexes as a second migration
# Open models.py (indices already declared) and run:
flask db migrate -m "add indexes"
flask db upgrade

# Seed some sample data
python seed.py

# Run the app
flask run
```

Visit http://127.0.0.1:5000/ (root) and http://127.0.0.1:5000/api/users

---

## 4) API Endpoints

Base URL: `http://localhost:5000/api`

| Endpoint                      | Method | Description                                | Body / Params                      |
|-------------------------------|--------|--------------------------------------------|------------------------------------|
| `/users`                      | GET    | List users (paginated)                     | `?page=1&per_page=20`              |
| `/users`                      | POST   | Create user                                | JSON: `username`, `email`, `bio?`  |
| `/users/<id>`                 | GET    | Get one user                               | —                                  |
| `/users/<id>`                 | PUT    | Update user or profile bio                 | JSON: `username?`, `email?`, `bio?`|
| `/users/<id>`                 | DELETE | Delete user (cascade deletes posts/likes)  | —                                  |
| `/posts`                      | GET    | List posts (filter/search)                 | `?topic=...&q=...&page=&per_page=` |
| `/posts`                      | POST   | Create post                                | JSON: `author_id`, `topic`, `content` |
| `/posts/<id>`                 | GET    | Get one post                               | —                                  |
| `/posts/<id>`                 | PUT    | Update post                                | JSON: `topic?`, `content?`         |
| `/posts/<id>`                 | DELETE | Delete post                                | —                                  |
| `/posts/<id>/like`            | POST   | Like a post                                | JSON: `user_id`                    |
| `/posts/<id>/unlike`          | POST   | Unlike a post                              | JSON: `user_id`                    |
| `/stats/posts-by-topic`       | GET    | Aggregated counts by topic                 | —                                  |

### Notes on performance
- We add a **B-Tree index** on `posts(topic, created_at)` and individual indexes for `posts.topic`, `posts.created_at`, `posts.author_id`.
- `users.email` and `users.username` are unique & indexed.
- Use query parameters (`topic`, `q`, pagination) to reduce result set sizes.

---

## 5) Insomnia collection

Import `insomnia_collection.json` into Insomnia. It has requests pre-configured for all endpoints.

---

## 6) Optional: Data visualization via Colab + Ngrok

1. Start an ngrok TCP tunnel to your local Postgres on port 5432:
   ```bash
   ngrok config add-authtoken <YOUR_TOKEN>
   ngrok tcp 5432
   ```
   Note the forwarding host and port printed by ngrok.
2. Open `data_viz/colab_visualization_snippet.py`, paste your forwarding host/port, and run it in Google Colab.

---

## 7) Dump your database
```bash
# Linux/macOS
./scripts/pg_dump.sh

# Windows PowerShell example
# Adjust path to pg_dump.exe if necessary
scripts\pg_dump.ps1
```

---

## 8) ER Diagram (Mermaid)
```mermaid
erDiagram
    users ||--|| profiles : "1-1"
    users ||--o{ posts : "1-many"
    users }o--o{ posts : "likes (m2m)"

    users {{
      int id PK
      string username
      string email
      datetime created_at
    }}

    profiles {{
      int id PK
      text bio
      int user_id FK UNIQUE
    }}

    posts {{
      int id PK
      string topic
      text content
      datetime created_at
      int author_id FK
    }}
```

---

## 9) Future improvements
- Auth (JWT), pagination links, rate limiting
- Caching for heavy aggregates
- Background jobs for analytics

---

## License
MIT (educational template)
