def sort_array(array, pivot):
    sorted_array = array.copy()
    sorted_array = sorted_array[:pivot] + sorted_array[pivot + 1:] + [sorted_array[pivot]]
    if (sorted_array[0] + sorted_array[pivot]) % 2 == 0:
        sorted_array[:pivot] = sorted(sorted_array[:pivot], reverse=True)
    else:
        sorted_array[:pivot] = sorted(sorted_array[:pivot])
    if (sorted_array[0] + sorted_array[pivot]) % 2 == 0:
        sorted_array[pivot + 1:] = sorted(sorted_array[pivot + 1:])
    else:
        sorted_array[pivot + 1:] = sorted(sorted_array[pivot + 1:], reverse=True)
    return sorted_array