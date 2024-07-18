
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 1 upto n inclusive.
    >>> string_sequence(1)
    '1'
    >>> string_sequence(5)
    '1 2 3 4 5'
    """
    return ' '.join((str(i) for i in range(1, n + 1)))