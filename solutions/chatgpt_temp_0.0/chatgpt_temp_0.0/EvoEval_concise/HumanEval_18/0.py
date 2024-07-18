

def how_many_times(string: str, substring: str) -> int:
    """ Returns the count of the occurrences of the substring in the string, including overlaps.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if len(substring) == 0:
        return count
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count