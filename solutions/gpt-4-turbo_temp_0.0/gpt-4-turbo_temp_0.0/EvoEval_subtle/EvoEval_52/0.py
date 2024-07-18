

def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below or equal to threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 20)
    True
    """
    return all((x <= t for x in l))