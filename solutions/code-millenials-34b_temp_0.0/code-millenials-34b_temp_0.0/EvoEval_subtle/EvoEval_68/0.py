
def pluck(arr):
    smallest_odd_value = float('inf')
    smallest_odd_index = float('inf')
    for (i, value) in enumerate(arr):
        if value % 2 == 1 and value < smallest_odd_value:
            smallest_odd_value = value
            smallest_odd_index = i
    if smallest_odd_index == float('inf'):
        return []
    else:
        return [smallest_odd_index, smallest_odd_value]