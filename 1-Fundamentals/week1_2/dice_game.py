import random

# Global variable
high_score = 0

def dicegame():
    global high_score  # Access the global high_score variable

    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")

        if choice == "1":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            total = die1 + die2
            print(f"\nYou rolled a {die1} and a {die2}. Total: {total}")

            if total > high_score:
                high_score = total
                print("New high score!\n")
            else:
                print()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1 or 2.\n")

# Call the function
dicegame()
