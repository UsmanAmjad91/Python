# donations_pkg/homepage.py
def show_homepage() -> None:
    print("\n=== DonateMe Homepage ===")
    print("--------------------------")
    print("| 1.  Login    | 2. Register |")
    print("--------------------------")
    print("| 3.  Donate   | 4. Show Donations |")
    print("--------------------------")
    print("|            5. Exit            |")
    print("--------------------------")


def donate(username: str) -> str:
    """Prompt for a positive numeric amount and return a formatted donation string."""
    while True:
        try:
            donation_amt = float(input("Enter amount to donate: "))
            if donation_amt <= 0:
                print("Donation must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter numbers only (e.g. 25 or 25.50).")

    donation_string = f"{username} donated ${donation_amt:.2f}"
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations: list[str]) -> None:
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
        return

    total = 0.0
    for d in donations:
        print(d)
        # each string ends with "$<amount>", so split & add
        total += float(d.split("$")[-1])
    print(f"\nTotal raised: ${total:,.2f}")
