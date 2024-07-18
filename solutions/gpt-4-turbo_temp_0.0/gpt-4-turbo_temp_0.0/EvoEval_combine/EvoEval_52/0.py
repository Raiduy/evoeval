def pluck_and_prod(arr):
    if not arr or all((num % 2 != 0 for num in arr)):
        return ([], None)
    smallest_even = None
    index_of_smallest_even = None
    for (i, num) in enumerate(arr):
        if num % 2 == 0 and (smallest_even is None or num < smallest_even):
            smallest_even = num
            index_of_smallest_even = i
    plucked_node = [smallest_even, index_of_smallest_even]
    arr.pop(index_of_smallest_even)
    if not arr:
        return (plucked_node, None)
    sum_of_magnitudes = sum((abs(num) for num in arr))
    product_of_signs = 1
    for num in arr:
        if num < 0:
            product_of_signs *= -1
        elif num == 0:
            product_of_signs = 0
            break
    return (plucked_node, sum_of_magnitudes * product_of_signs)