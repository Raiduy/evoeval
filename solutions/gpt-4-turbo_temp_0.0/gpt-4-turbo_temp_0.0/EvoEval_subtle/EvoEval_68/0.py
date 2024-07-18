
def pluck(arr):
    smallest_odd = None
    smallest_odd_index = -1
    for (i, value) in enumerate(arr):
        if value % 2 != 0 and (smallest_odd is None or value < smallest_odd):
            smallest_odd = value
            smallest_odd_index = i
    if smallest_odd is not None:
        return [smallest_odd_index, smallest_odd]
    else:
        return []