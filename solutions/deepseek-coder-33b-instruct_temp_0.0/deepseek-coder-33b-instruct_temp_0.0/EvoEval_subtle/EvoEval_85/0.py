
def add(lst):
    """Given a non-empty list of integers lst, add the odd elements that are at even indices.

    Examples:
        add([4, 2, 5, 7]) ==> 5
    """
    return sum((val for (idx, val) in enumerate(lst) if idx % 2 == 0 and val % 2 != 0))