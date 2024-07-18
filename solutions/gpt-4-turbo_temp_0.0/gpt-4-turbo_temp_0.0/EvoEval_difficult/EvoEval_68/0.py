def pluck_and_replace(arr, replacement):
    if replacement in arr:
        return [-1, -1, replacement, -1]
    smallest_even = float('inf')
    index_of_smallest_even = -1
    for (i, value) in enumerate(arr):
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            index_of_smallest_even = i
    if smallest_even == float('inf'):
        return []
    arr[index_of_smallest_even] = replacement
    return [smallest_even, index_of_smallest_even, replacement, index_of_smallest_even]