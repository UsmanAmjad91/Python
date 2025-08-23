# def test():
#     value1= input("Enter first value: ")
#     value2 = input("Enter second value: ")
#     sum = int(value1) + int(value2);
#     return sum;


# print("The sum is: ", test())
# for i in range(10):
#     print("This is a loop iteration: " + str(i))

while True:
    try:
        value1 = input("Enter first value: ")
        value2 = input("Enter second value: ")
        sum = int(value1) + int(value2)
        print("The sum is:", sum)
        break
    except ValueError:
        print("Invalid input. Please enter numeric values.")