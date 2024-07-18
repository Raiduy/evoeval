
def sort_array(array):
    if not array:
        return []
    elif len(array) == 1:
        return array
    else:
        sum_first_last = array[0] + array[-1]
        if sum_first_last % 2 == 0:
            sorted_array = sorted(set(array), reverse=True)
        else:
            sorted_array = sorted(set(array))
        return sorted_array