def sort_array(array, pivot):
    if not array:
        return []
    pivot_value = array[pivot]
    less = [x for x in array if x < pivot_value]
    equal = [x for x in array if x == pivot_value]
    greater = [x for x in array if x > pivot_value]
    if (less[0] if less else 0 + pivot_value) % 2 == 0:
        return sorted(less, reverse=True) + equal + sorted(greater)
    else:
        return sorted(less) + equal + sorted(greater, reverse=True)