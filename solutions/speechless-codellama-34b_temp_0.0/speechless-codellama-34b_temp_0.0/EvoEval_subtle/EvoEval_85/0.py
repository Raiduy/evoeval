
def add(lst):
    """Given a non-empty list of integers lst, add the odd elements that are at even indices.

    Examples:
        add([4, 2, 5, 7]) ==> 5
    """
    result = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            result += lst[i]
    return result