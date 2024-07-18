
def pluck(arr):
    if not arr:
        return []
    smallest_even_value = float('inf')
    smallest_even_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]
            smallest_even_index = i
    if smallest_even_index == -1:
        return []
    return [smallest_even_value, smallest_even_index]