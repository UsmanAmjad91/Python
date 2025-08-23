# app.py
from donations_pkg.homepage import (
    show_homepage,
    donate,
    show_donations,
)
from donations_pkg.user import login, register, _normalize  # type: ignore

# ---------------------------------------------------------------------
# “Database” & application state
# ---------------------------------------------------------------------
database: dict[str, str] = {"admin": "password123"}   # username : password
donations: list[str] = []
authorized_user: str = ""

# ------------------------------------------------------------------
# Main event‑loop wrapped in a function
# ------------------------------------------------------------------
def _main_(database: dict[str, str],
           donations: list[str],
           authorized_user: str) -> str:
    """Run the menu loop.  
    Returns the username that was logged‑in when the user quit,
    or the empty string if no one was signed in.
    """
    while True:
        show_homepage()

        # status banner
        if authorized_user == "":
            print("You must be logged in to donate.\n")
        else:
            print(f"Logged in as: {authorized_user}\n")

        choice = input("Choose an option: ")

        # ---------------------------- 1. Login
        if choice == "1":
            if authorized_user:            # already logged‑in guard
                print(f"You are already logged in as {authorized_user}.\n")
                continue

            username = input("\nEnter username: ")
            password = input("Enter password: ")
            authorized_user = login(database, username, password)

        # ---------------------------- 2. Register
        elif choice == "2":
            username = input("\nEnter username: ")
            password = input("Enter password: ")

            new_user = register(database, username)
            if new_user:                   # registration succeeded
                if len(password) < 5:
                    print("Password must be at least 5 characters long.")
                else:
                    database[_normalize(new_user)] = password
                    authorized_user = new_user

        # ---------------------------- 3. Donate
        elif choice == "3":
            if authorized_user == "":
                print("You are not logged in.\n")
            else:
                donation_string = donate(authorized_user)
                donations.append(donation_string)

        # ---------------------------- 4. Show Donations
        elif choice == "4":
            show_donations(donations)

        # ---------------------------- 5. Exit
        elif choice == "5":
            print("\nLeaving DonateMe… Thank you! Good‑bye!")
            return authorized_user        # <-- function exits here

        # ---------------------------- invalid choice
        else:
            print("Please choose a valid option 1‑5.")


# ------------------------------------------------------------------
# Run the program only if this file is executed directly
# ------------------------------------------------------------------
if __name__ == "__main__":
    final_user = _main_(database, donations, authorized_user)
    