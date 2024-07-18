
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices."""
    return sum(val for idx, val in enumerate(lst) if idx % 2 != 0 and val % 2 == 0)
