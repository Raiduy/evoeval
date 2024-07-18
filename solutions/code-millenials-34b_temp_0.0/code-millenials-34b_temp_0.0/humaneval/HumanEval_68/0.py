
def pluck(arr):
    smallest_even_value = float('inf')
    smallest_index = 0

    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_index = i

    if smallest_even_value == float('inf'):
        # This means there was no even value in the list
        return []
    else:
        return [smallest_even_value, smallest_index]
