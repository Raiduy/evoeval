def sort_array(array, pivot):
    arr = array[:]
    pivot_value = arr[pivot]
    less = [x for x in arr if x < pivot_value]
    greater = [x for x in arr if x > pivot_value]
    if less:
        if (less[0] + pivot_value) % 2 == 0:
            less.sort(reverse=True)
            greater.sort()
        else:
            less.sort()
            greater.sort(reverse=True)
    else:
        greater.sort()
    result = less + [pivot_value] + greater
    return result