def pluck_and_replace(arr, replacement):
    if not arr or replacement in arr:
        return [-1, -1, replacement, -1]
    even_values = [x for x in arr if x % 2 == 0 and x != replacement]
    if not even_values:
        return []
    smallest_even_value = min(even_values)
    smallest_even_index = arr.index(smallest_even_value)
    arr[smallest_even_index] = replacement
    return [smallest_even_value, smallest_even_index, replacement, arr.index(replacement)]