def generate_pattern(n: int):
    """
    Given an integer 'n', return a list of strings where each string represents a pattern. 
    The pattern is composed of the numbers from 1 to n in ascending order, then descending back to 1, 
    with each number separated by a comma. If n is 0 or negative, return an empty list.

    >>> generate_pattern(3)
    ['1', '1,2', '1,2,3', '3,2,1', '2,1', '1']

    >>> generate_pattern(0)
    []
    """
    if n <= 0:
        return []
    pattern = []
    for i in range(1, n + 1):
        pattern.append(','.join((str(j) for j in range(1, i + 1))))
    for i in range(n, 0, -1):
        pattern.append(','.join((str(j) for j in range(i, 0, -1))))
    return pattern