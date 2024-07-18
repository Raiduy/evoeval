
def pluck(arr):
    min_odd = float('inf')
    min_index = float('inf')
    for (i, num) in enumerate(arr):
        if num % 2 != 0 and num < min_odd:
            min_odd = num
            min_index = i
    if min_odd == float('inf'):
        return []
    else:
        return [min_index, min_odd]