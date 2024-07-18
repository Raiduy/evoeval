
def sort_array(array):
    unique_array = list(set(array))
    if len(unique_array) <= 1:
        return unique_array
    if (unique_array[0] + unique_array[-1]) % 2 == 0:
        sorted_array = sorted(unique_array, reverse=True)
    else:
        sorted_array = sorted(unique_array)
    return sorted_array