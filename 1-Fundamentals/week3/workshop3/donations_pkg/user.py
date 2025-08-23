# donations_pkg/user.py
import re


def _normalize(username: str) -> str:
    """Helper: return a lower‑cased version for case‑insensitive look‑ups."""
    return username.lower()


def login(database: dict[str, str], username: str, password: str) -> str:
    key = _normalize(username)
    if key in database:
        if database[key] == password:
            print(f"\nWelcome back, {username}!")
            return username
        else:
            print("\nIncorrect password for", username + ".")
            return ""
    print("\nUsername", username, "not found.")
    return ""


def register(database: dict[str, str], username: str) -> str:
    key = _normalize(username)

    # length & character validation
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", username):
        print("Username must start with a letter and contain only letters & digits.")
        return ""
    if len(username) > 10:
        print("Username cannot exceed 10 characters.")
        return ""
    if key in database:
        print("Username already registered.")
        return ""

    print(f"\nUsername {username} registered!")
    return username
