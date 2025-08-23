x = 0

while x <= 10:
    if x < 5:
        print(x)
    elif x >= 5 and x <= 8 and x != 6:
        print(f"x is bigger or equal to 5, and less or equal to 8, but not 6. It is: {x}")
    elif x == 6:
        print(x)
        x += 1  # To prevent skipping increment due to continue
        continue
    else:
        print(f"x is bigger than 8. It is: {x}")
    
    x += 1
