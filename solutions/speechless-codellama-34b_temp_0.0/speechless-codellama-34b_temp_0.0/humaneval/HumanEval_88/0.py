
def sort_array(array):
    if not array:
        return []
    elif len(array) == 1:
        return array
    else:
        if (array[0] + array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)
