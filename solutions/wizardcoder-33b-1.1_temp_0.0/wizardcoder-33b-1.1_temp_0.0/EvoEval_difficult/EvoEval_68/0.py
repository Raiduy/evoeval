def pluck_and_replace(arr, replacement):
    if not arr:
        return []
    if replacement in arr:
        return [-1, -1, replacement, -1]
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    smallest_value = min(even_values)
    index = arr.index(smallest_value)
    arr[index] = replacement
    return [smallest_value, index, replacement, arr.index(replacement)]