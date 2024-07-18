def pluck_and_replace(arr, replacement):
    smallest_even = float('inf')
    smallest_index = -1
    for (i, num) in enumerate(arr):
        if num == replacement:
            return [-1, -1, replacement, -1]
        elif num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_index = i
    if smallest_index == -1:
        return []
    else:
        arr[smallest_index] = replacement
        return [smallest_even, smallest_index, replacement, smallest_index]