def next_smallest_and_largest(lst):
    if len(lst) < 2:
        return (None, None)
    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst:
        if num < smallest:
            (second_smallest, smallest) = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
        if num > largest:
            (second_largest, largest) = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return (second_smallest if second_smallest != float('inf') else None, second_largest if second_largest != float('-inf') else None)