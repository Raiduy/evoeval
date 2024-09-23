
def pluck(arr):
    smallest_even = float('inf')
    smallest_index = -1
    for (i, val) in enumerate(arr):
        if val % 2 == 0 and val < smallest_even:
            smallest_even = val
            smallest_index = i
    if smallest_index == -1:
        return []
    else:
        return [smallest_even, smallest_index]