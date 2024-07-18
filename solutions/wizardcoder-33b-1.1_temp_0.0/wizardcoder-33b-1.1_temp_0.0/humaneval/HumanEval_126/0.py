
def is_sorted(lst):
    # Check if list has more than 1 duplicate of the same number
    if len(lst) != len(set(lst)):
        return False
    # Check if list is sorted in ascending order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
