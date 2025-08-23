import random

# A “mini‑deck” containing all thirteen diamonds
diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

# The player’s hand starts empty
hand = []

# Keep looping as long as there is at least one card left in diamonds
while diamonds:
    user_input = input("Press enter to pick a card, or Q then enter to quit: ").strip().upper()

    # Exit the loop if the user types Q (or q)
    if user_input == "Q":
        break

    # Randomly select a card still in the deck
    card = random.choice(diamonds)

    # Remove it from the diamonds list and add it to the hand
    diamonds.remove(card)
    hand.append(card)

    # Show current state
    print(f"Your hand: {hand}")
    print(f"Remaining cards: {diamonds}")

# After the loop ends, check whether the deck is empty
if not diamonds:
    print("There are no more cards to pick.")
