
def add(lst):
    """Sum the even numbers at odd indices in a non-empty list of integers, lst."""
    return sum((val for (i, val) in enumerate(lst) if i % 2 != 0 and val % 2 == 0))