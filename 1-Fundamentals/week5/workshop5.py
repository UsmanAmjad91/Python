import random
#Muhammad Usman Amjad

# Workshop 5 

# Implements the three required workshop tasks:
#   1. Human guesses a random number                -> guess_random_number()
#   2. Program guesses using linear search          -> guess_random_num_linear()
#   3. Program guesses using binary search          -> guess_random_num_binary()

def _get_int(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt)
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if min_value is not None and val < min_value:
            print(f"Value must be >= {min_value}.")
            continue
        if max_value is not None and val > max_value:
            print(f"Value must be <= {max_value}.")
            continue
        return val
#human
def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    guessed_numbers = set()
    print(f"Guess the number between {start} and {stop}.")
    while tries > 0:
        print(f"Number of tries left: {tries}")
        try:
            guess = int(input(f"Guess a number between {start} and {stop}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess < start or guess > stop:
            print(f"Out of range! Please enter a number between {start} and {stop}.")
            continue
        if guess in guessed_numbers:
            print("You already guessed that number! Try something new.")
            continue
        guessed_numbers.add(guess)
        if guess == target:
            print("You guessed the correct number!")
            return
        elif guess < target:
            print("Guess higher!")
        else:
            print("Guess lower!")
        tries -= 1
    print(f"You have failed to guess the number: {target}")
#Linear
def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print(f"The number for the program to guess is: {target}")
    for num in range(start, stop + 1):
        if tries <= 0:
            print("The program has failed to guess the correct number.")
            return
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing... {num}")
        if num == target:
            print("The program has guessed the correct number!")
            return
        tries -= 1
    print("The program has failed to guess the correct number.")
#binary
def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    print(f"The number for the program to guess is: {target}")
    low = start
    high = stop
    while tries > 0 and low <= high:
        print(f"Number of tries left: {tries}")
        mid = (low + high) // 2
        print(f"The program is guessing... {mid}")
        if mid == target:
            print("The program has guessed the correct number!")
            return
        elif mid < target:
            print("Guessing higher...")
            low = mid + 1
        else:
            print("Guessing lower...")
            high = mid - 1
        tries -= 1
    print("The program has failed to guess the correct number.")

def run_menu():
    print("\n=== Guess the Number Workshop ===")
    print("1) Human guesses")
    print("2) Program guesses (Linear Search)")
    print("3) Program guesses (Binary Search)")
    print("Q) Quit")
    choice = input("Select an option: ").strip().lower()
    if choice == 'q':
        print("Goodbye!")
        return
    start = _get_int("Enter start of range (int): ")
    stop = _get_int("Enter end of range (int): ")
    while stop < start:
        print("End of range must be >= start.")
        stop = _get_int("Enter end of range (int): ")
    tries = _get_int("Enter number of tries (int > 0): ", 1)
    print()
    if choice == '1':
        guess_random_number(tries, start, stop)
    elif choice == '2':
        guess_random_num_linear(tries, start, stop)
    elif choice == '3':
        guess_random_num_binary(tries, start, stop)
    else:
        print("Invalid selection.")

def driver_task1():
    guess_random_number(5, 0, 10)

def driver_task2():
    guess_random_num_linear(5, 0, 10)

def driver_task3():
    guess_random_num_binary(5, 0, 100)

if __name__ == "__main__":
    run_menu()
