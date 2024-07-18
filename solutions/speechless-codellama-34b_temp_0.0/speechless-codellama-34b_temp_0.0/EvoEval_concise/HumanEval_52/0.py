

def below_threshold(l: list, t: int) -> bool:
    """Checks if all elements in list l are less than threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for element in l:
        if element >= t:
            return False
    return True