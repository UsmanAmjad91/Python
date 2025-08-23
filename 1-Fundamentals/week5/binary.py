def binary_search(the_list,target):
    low = 0
    high = len(the_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = the_list[mid]

        if guess == target:
            print("Target found at index:", mid)
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    print("Target not found.", target)
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
binary_search(my_list, 7)  
binary_search(my_list, 20)  # should print: Target not found.