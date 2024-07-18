
def pluck(arr):
    smallest_odd = float('inf')
    smallest_odd_index = float('inf')
    for (i, num) in enumerate(arr):
        if num % 2 != 0 and num < smallest_odd:
            smallest_odd = num
            smallest_odd_index = i
    if smallest_odd == float('inf'):
        return []
    return [smallest_odd_index, smallest_odd]