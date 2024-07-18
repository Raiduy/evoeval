
def next_largest(lst):
    (first, second) = (float('-inf'), float('-inf'))
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    if second == float('-inf'):
        return None
    else:
        return second