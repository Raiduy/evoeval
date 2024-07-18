
def next_smallest(lst):
    if len(lst) < 2:
        return None
    smallest = lst[0]
    second_smallest = None
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest
