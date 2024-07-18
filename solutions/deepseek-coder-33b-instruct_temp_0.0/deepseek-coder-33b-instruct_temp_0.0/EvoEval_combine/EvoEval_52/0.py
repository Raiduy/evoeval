def pluck_and_prod(arr):
    if not arr:
        return ([], None)
    min_even = float('inf')
    min_index = -1
    for (i, num) in enumerate(arr):
        if num % 2 == 0 and num < min_even:
            min_even = num
            min_index = i
    if min_index == -1:
        return ([], None)
    arr.pop(min_index)
    if not arr:
        return ([min_even, min_index], None)
    product = 1
    sum_magnitude = 0
    for num in arr:
        product *= 1 if num == 0 else -1 if num < 0 else 1
        sum_magnitude += abs(num)
    return ([min_even, min_index], product * sum_magnitude)