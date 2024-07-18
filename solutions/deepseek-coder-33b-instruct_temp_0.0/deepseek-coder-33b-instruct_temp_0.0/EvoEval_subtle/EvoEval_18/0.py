
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Do not count overlapping cases.
    
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    2
    """
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + len(substring)
            count += 1
        else:
            break
    return count