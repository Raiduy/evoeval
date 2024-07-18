
def next_largest(lst):
    if len(lst) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest