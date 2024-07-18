def pluck_and_prod(arr):
    if not arr:
        return ([], None)
    smallest_value = min(filter(lambda x: x % 2 == 0, arr), default=None)
    if smallest_value is None:
        return ([], None)
    smallest_index = arr.index(smallest_value)
    arr.remove(smallest_value)
    remaining_sum = sum(map(lambda x: abs(x) * (1 if x > 0 else -1), arr))
    return ([smallest_value, smallest_index], remaining_sum)