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
    sum_remaining = sum((abs(num) for num in arr))
    prod_signs = -1 if any((num < 0 for num in arr)) else 1
    return ([min_even, min_index], sum_remaining * prod_signs)