def sort_array(array, pivot):
    array_copy = array[:]
    pivot_value = array_copy[pivot]
    less_part = [x for x in array_copy if x < pivot_value]
    equal_part = [x for x in array_copy if x == pivot_value]
    greater_part = [x for x in array_copy if x > pivot_value]
    if sum([less_part[0], pivot_value]) % 2 == 0:
        less_part.sort(reverse=True)
    else:
        less_part.sort()
    result = less_part + equal_part + greater_part
    return result