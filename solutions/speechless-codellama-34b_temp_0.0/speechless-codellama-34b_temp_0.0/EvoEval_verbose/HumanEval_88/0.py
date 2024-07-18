
def sort_array(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array
    else:
        sum_first_last = array[0] + array[-1]
        if sum_first_last % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)