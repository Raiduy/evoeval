def pluck_and_prod(arr):
    if not arr:
        return ([], None)
    smallest_even = min(((v, i) for (i, v) in enumerate(arr) if v % 2 == 0)) if any((v % 2 == 0 for v in arr)) else None
    if smallest_even is None:
        return ([], None)
    arr.pop(smallest_even[1])
    if not arr:
        return ([smallest_even[0], smallest_even[1]], None)
    sum_magnitude = sum((abs(v) for v in arr))
    product_signs = 1 if all((v >= 0 for v in arr)) else -1 if sum((1 for v in arr if v < 0)) % 2 else 0
    return ([smallest_even[0], smallest_even[1]], sum_magnitude * product_signs)