import random

pips = random.randint(1, 6)
print("Random number between 1 and 6:", pips)


prizes = ["Car", "Bike", "Watch", "Phone"]
prize = random.choice(prizes)
print("Randomly selected prize:", prize)


cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
print("Shuffled cards:", cards)