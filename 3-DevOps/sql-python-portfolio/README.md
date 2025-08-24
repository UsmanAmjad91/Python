# SQL-Python Portfolio (cleaned)

## What this project contains
- Flask API with Users, Posts, Likes
- Secure password hashing
- Session (cookie) based login
- Migrations via Flask-Migrate
- Seed script to generate demo data
- Insomnia collection included

## Setup (Windows PowerShell)

1. Create and activate virtualenv:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Copy .env file and edit DATABASE_URL:
   ```powershell
   copy .env.example .env
   # edit .env and set correct DATABASE_URL, SECRET_KEY
   ```

4. Ensure Postgres is running and create DB:
   ```sql
   CREATE DATABASE sql_python_portfolio;
   ```

5. Initialize and run migrations:
   ```powershell
   flask db init
   flask db migrate -m "Initial schema"
   flask db upgrade
   ```

6. (Optional) Seed demo data:
   ```powershell
   python seed.py
   ```

7. Run:
   ```powershell
   flask run
   ```

8. Visit:
   - http://127.0.0.1:5000/  (base message)
   - http://127.0.0.1:5000/api/  (API root)
