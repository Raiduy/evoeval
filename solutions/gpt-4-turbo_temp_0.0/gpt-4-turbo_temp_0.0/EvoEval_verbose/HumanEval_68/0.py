
def pluck(arr):
    smallest_even = float('inf')
    index_of_smallest_even = -1
    for (index, value) in enumerate(arr):
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            index_of_smallest_even = index
    if smallest_even == float('inf'):
        return []
    else:
        return [smallest_even, index_of_smallest_even]