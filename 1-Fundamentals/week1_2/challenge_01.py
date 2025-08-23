# Challenge 01: Basic Python Syntax
print("This is a string")
a = 5
print(type(a))  # prints the type of variable a
b = 3.14         # float value assigned to b
print(type(b))   # prints the type of variable b
c = "Hello"      # string value assigned to c
print(type(c))   # prints the type of variable c
d = a + b        # adding integer a and float b
print(d)         # prints the actual value of d

# Challenge 02: Basic Python Syntax
	

gradeToTest = int(input("Enter your Grade: "))  # Convert input to an integer
if gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90:
    print("A")
elif gradeToTest >= 80:
    print("B")
elif gradeToTest >= 70:
    print("C")
elif gradeToTest >= 50:
    print("D")
else:
    print("F")

# Challenge 03: Basic Python Syntax
	
priceIsRight = int(input("Enter your guess for the price: "))  # Convert input to an integer

if priceIsRight < 5:
    print("That's too low!")
elif priceIsRight >= 5 and priceIsRight <= 9:
    print("Getting warmer...")
elif priceIsRight == 10:
    print("Correct! You win!")
else:
    print("That's too high!")

    # Challenge 04: Basic Python Syntax
    	
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

    # Challenge 05: Basic Python Syntax
    

