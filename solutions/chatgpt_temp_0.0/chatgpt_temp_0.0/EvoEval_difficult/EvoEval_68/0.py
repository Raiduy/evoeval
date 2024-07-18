def pluck_and_replace(arr, replacement):
    if replacement in arr:
        return [-1, -1, replacement, -1]
    even_values = [num for num in arr if num % 2 == 0 and num != replacement]
    if not even_values:
        return []
    smallest_even = min(even_values)
    smallest_even_index = arr.index(smallest_even)
    return [smallest_even, smallest_even_index, replacement, smallest_even_index]