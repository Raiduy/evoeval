
def unique(l: list):
    """Return sorted unique elements in a list in descending order
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [123, 9, 5, 3, 2, 0]
    """
    unique_elements = list(set(l))
    unique_elements.sort(reverse=True)
    return unique_elements