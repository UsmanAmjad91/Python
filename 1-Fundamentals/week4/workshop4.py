class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        if (
            isinstance(new_name, str)
            and 2 <= len(new_name) <= 10
            and new_name != self.name
            and " " not in new_name
        ):
            self.name = new_name
        else:
            print("Invalid name. Must be 2-10 chars, no spaces, and different from current.")

    def change_pin(self, new_pin):
        if (
            isinstance(new_pin, int)
            and 1000 <= new_pin <= 9999
            and new_pin != self.pin
        ):
            self.pin = new_pin
        else:
            print("Invalid PIN. Must be exactly 4 digits and different from current.")

    def change_password(self, new_password):
        if (
            isinstance(new_password, str)
            and len(new_password) >= 5
            and new_password != self.password
            and " " not in new_password
        ):
            self.password = new_password
        else:
            print("Invalid password. Must be at least 5 chars, no spaces, and different from current.")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.0
        self.on_hold = False

    def show_balance(self):
        print(f"Balance for {self.name}: ${self.balance:.2f}")

    def deposit(self, amount):
        if self.on_hold:
            print(f"Transaction failed: Account for {self.name} is on hold.")
            return
        if not (isinstance(amount, (int, float)) and amount > 0):
            print("Deposit failed: Amount must be a positive number.")
            return
        self.balance += amount
        print(f"${amount:.2f} deposited to {self.name}'s account.")

    def withdraw(self, amount):
        if self.on_hold:
            print(f"Transaction failed: Account for {self.name} is on hold.")
            return
        if not (isinstance(amount, (int, float)) and amount > 0):
            print("Withdrawal failed: Amount must be a positive number.")
            return
        if amount > self.balance:
            print("Withdrawal failed: Insufficient funds.")
            return
        self.balance -= amount
        print(f"${amount:.2f} withdrawn from {self.name}'s account.")

    def transfer_money(self, amount, other_user, pin):
        if self.on_hold or other_user.on_hold:
            print("Transaction failed: One or both accounts are on hold.")
            return False
        if pin != self.pin:
            print("Transfer failed: Incorrect PIN.")
            return False
        if not (isinstance(amount, (int, float)) and amount > 0):
            print("Transfer failed: Amount must be positive.")
            return False
        if amount > self.balance:
            print("Transfer failed: Insufficient funds.")
            return False
        self.balance -= amount
        other_user.balance += amount
        print(f"${amount:.2f} transferred from {self.name} to {other_user.name}.")
        return True

    def request_money(self, amount, from_user, pin, password):
        if self.on_hold or from_user.on_hold:
            print("Transaction failed: One or both accounts are on hold.")
            return False
        if pin != self.pin:
            print("Request failed: Incorrect PIN.")
            return False
        if password != from_user.password:
            print("Request failed: Incorrect password.")
            return False
        if not (isinstance(amount, (int, float)) and amount > 0):
            print("Request failed: Amount must be positive.")
            return False
        if amount > from_user.balance:
            print("Request failed: Insufficient funds in sender's account.")
            return False
        from_user.balance -= amount
        self.balance += amount
        print(f"${amount:.2f} requested from {from_user.name} to {self.name} completed.")
        return True

    def toggle_hold(self):
        self.on_hold = not self.on_hold
        status = "on hold" if self.on_hold else "active"
        print(f"Account for {self.name} is now {status}.")


# """ Driver Code for Task 1 """
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)

# """ Driver Code for Task 2 """
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
user1.change_name("Rob")
user1.change_pin(4321)
user1.change_password("newpass")
print(user1.name, user1.pin, user1.password)

# """ Driver Code for Task 3 """
bank_user1 = BankUser("Alice", 1111, "alicepwd")
print(bank_user1.name, bank_user1.pin, bank_user1.password, bank_user1.balance)

# """ Driver Code for Task 4 """
bank_user1 = BankUser("Alice", 1111, "alicepwd")
bank_user1.show_balance()
bank_user1.deposit(1000)
bank_user1.show_balance()
bank_user1.withdraw(200)
bank_user1.show_balance()

# """ Driver Code for Task 5 """
user1 = BankUser("Alice", 1111, "alicepwd")
user2 = BankUser("Bob", 2222, "bobpwd")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
if user2.transfer_money(500, user1, 2222):
    user2.show_balance()
    user1.show_balance()
    if user2.request_money(200, user1, 1111, "alicepwd"):
        user2.show_balance()
        user1.show_balance()

# """ Driver Code for Bonus: on_hold toggle and transaction rejection """
user3 = BankUser("Charlie", 3333, "charliepwd")
user3.deposit(1000)
user3.show_balance()
user3.toggle_hold()          # Puts account on hold
user3.withdraw(100)          # Should fail due to hold
user3.toggle_hold()          # Reactivate account
user3.withdraw(100)          # Should succeed
user3.show_balance()
