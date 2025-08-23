
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
