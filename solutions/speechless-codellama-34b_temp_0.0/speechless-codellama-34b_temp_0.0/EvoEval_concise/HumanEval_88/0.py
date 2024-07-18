
def sort_array(array):
    if not array:
        return []
    elif len(array) == 1:
        return array
    else:
        sorted_array = sorted(array)
        if (sorted_array[0] + sorted_array[-1]) % 2 == 0:
            return sorted_array[::-1]
        else:
            return sorted_array