# Enhanced version with optional challenges
while True:
    # Character setup (same as before)
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    dwarf = "Dwarf"  # New character
    
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dwarf_hp = 120   # New character HP
    
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dwarf_damage = 80 # New character damage
    
    dragon_hp = 300
    dragon_damage = 50

    # Player selection
    while True:
        print("1)", wizard)
        print("2)", elf)
        print("3)", human)
        print("4)", dwarf)
        print("5) Exit Game")
        
        choice = input("Choose your character (1-4) or 5 to exit: ").lower()
        
        if choice in ["1", "wizard"]:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif choice in ["2", "elf"]:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif choice in ["3", "human"]:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif choice in ["4", "dwarf"]:  # New character option
            character = dwarf
            my_hp = dwarf_hp
            my_damage = dwarf_damage
            break
        elif choice in ["5", "exit"]:   # Exit option
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            print("Unknown character. Please try again.")
    
    # Battle sequence (same as before)
    print(f"\nYou have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}\n")
    
    while True:
        dragon_hp -= my_damage
        print(f"The {character} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon_hp}\n")
        
        if dragon_hp <= 0:
            print("The Dragon has lost the battle!")
            break
        
        my_hp -= dragon_damage
        print(f"The Dragon strikes back at {character}")
        print(f"The {character}'s hitpoints are now: {my_hp}\n")
        
        if my_hp <= 0:
            print(f"The {character} has lost the battle.")
            break
    
    # Play again option
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break