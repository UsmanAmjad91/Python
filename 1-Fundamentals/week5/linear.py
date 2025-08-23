
def linear_search(the_list, target):
    for i, value in enumerate(the_list):
        if value == target:
            print("Target found at index:", i)
            return i
    print("Target not found.",target)
    return i


my_list = [1, 2, 3, 4, 5]

linear_search(my_list, 3)  # should print: Target found at index: 2
linear_search(my_list, 7)  # should print: Target not found.
