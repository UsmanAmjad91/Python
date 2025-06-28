from banking_pkg import account

def atm_menu(name):
    print("")
    print("=== Automated Teller Machine ===")
    print(f"User: {name}")
    print("-------------------------------")
    print("| 1.    View Balance          |")
    print("| 2.    Deposit               |")
    print("| 3.    Withdraw              |")
    print("| 4.    Logout                |")
    print("-------------------------------")

# Registration
print("    === Automated Teller Machine ===    ")

# Validate name (1–10 characters)
while True:
    name = input("Enter name to register (1–10 chars): ")
    if 1 <= len(name) <= 15:
        break
    print("Invalid name length. Try again.")

# Validate PIN (4 digits only)
while True:
    pin = input("Enter 4-digit PIN: ")
    if len(pin) == 4 and pin.isdigit():
        break
    print("PIN must be exactly 4 digits. Try again.")

balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")

# Login loop
while True:
    print("\nLOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

# Menu loop
while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid option. Please try again.")
