def pluck_and_replace(arr, replacement):
    if not arr:
        return []
    if replacement in arr:
        return [-1, -1, replacement, -1]
    smallest_even_value = float('inf')
    smallest_even_index = -1
    for (i, value) in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_even_index = i
    if smallest_even_value == float('inf'):
        return []
    arr[smallest_even_index] = replacement
    return [smallest_even_value, smallest_even_index, replacement, smallest_even_index]