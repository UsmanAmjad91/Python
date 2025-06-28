def show_balance(balance):
    print(f"Your current balance is: ${balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
        return balance
    return balance - amount

def logout(name):
    print(f"Goodbye! Have a good day {name}")
