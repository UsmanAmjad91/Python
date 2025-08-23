# Task 1: Set Up the Game
wizard = "Wizard"
elf = "Elf"
human = "Human"

# Character HP
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Character Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon stats
dragon_hp = 300
dragon_damage = 50

# Task 2 & 3: Player Choice with infinite loop
while True:
    print("1)", wizard)
    print("2)", elf)
    print("3)", human)
    
    character = input("Choose your character: ").lower()
    
    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")

# Display chosen character stats
print(f"You have chosen the character: {character}")
print(f"Health: {my_hp}")
print(f"Damage: {my_damage}")
print()

# Task 4: Battle with the Dragon
while True:
    # Player attacks dragon
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}")
    print()
    
    # Check if dragon is defeated
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break
    
    # Dragon attacks player
    my_hp -= dragon_damage
    print(f"The Dragon strikes back at {character}")
    print(f"The {character}'s hitpoints are now: {my_hp}")
    print()
    
    # Check if player is defeated
    if my_hp <= 0:
        print(f"The {character} has lost the battle.")
        break