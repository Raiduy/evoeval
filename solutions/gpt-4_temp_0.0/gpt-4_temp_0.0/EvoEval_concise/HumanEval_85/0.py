
def add(lst):
    """Sum the even numbers at odd indices in a non-empty list of integers, lst.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum((num for (idx, num) in enumerate(lst) if idx % 2 != 0 and num % 2 == 0))