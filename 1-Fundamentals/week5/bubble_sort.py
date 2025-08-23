unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", unsorted_list)

def bubble_sort(the_list):
    highest_index = len(the_list) - 1
    for i in range(highest_index):
        for j in range(highest_index):
            item = the_list[j]
            next_item = the_list[j + 1]
            if item > next_item:
                the_list[j] = next_item
                the_list[j + 1] = item
    print("Intermediate state:", the_list,i, j)

sorted_list = bubble_sort(unsorted_list)

# def bubble_sort(the_list):
#     highest_index = len(the_list) - 1
#     for i in range(highest_index):
#         for j in range(highest_index):
#     #         if the_list[j] > the_list[j + 1]:
#     #             # Swap if the element found is greater than the next element
#     #             the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]
#     # return the_list 
# sorted_list = bubble_sort(unsorted_list)
# print("Sorted list:", sorted_list)
