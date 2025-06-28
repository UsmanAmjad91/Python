priceIsRight = int(input("Enter your guess for the price: "))  # Convert input to an integer

if priceIsRight < 5:
    print("That's too low!")
elif priceIsRight >= 5 and priceIsRight <= 9:
    print("Getting warmer...")
elif priceIsRight == 10:
    print("Correct! You win!")
else:
    print("That's too high!")