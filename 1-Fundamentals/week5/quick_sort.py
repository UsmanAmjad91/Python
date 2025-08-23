my_list=[5, 2, 9, 1, 5, 6]
print(my_list)

def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    else:
        pivot = the_list[0]
        less = [x for x in the_list[1:] if x <= pivot]
        greater = [x for x in the_list[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort(my_list))