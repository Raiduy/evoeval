def sort_array(array, pivot):
    copy_array = array[:]
    pivot_value = copy_array[pivot]
    (copy_array[pivot], copy_array[0]) = (copy_array[0], copy_array[pivot])
    i = 1
    for j in range(1, len(copy_array)):
        if copy_array[j] < pivot_value:
            (copy_array[i], copy_array[j]) = (copy_array[j], copy_array[i])
            i += 1
    (copy_array[0], copy_array[i - 1]) = (copy_array[i - 1], copy_array[0])
    if (copy_array[0] + pivot_value) % 2 == 1:
        copy_array[:i] = sorted(copy_array[:i])
    else:
        copy_array[:i] = sorted(copy_array[:i], reverse=True)
    copy_array[i:] = sorted(copy_array[i:])
    return copy_array