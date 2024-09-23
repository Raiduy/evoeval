def split_strings(s: str, n: int):
    """Return a list of n-character long strings created from the input string s.
    If the length of s isn't a multiple of n, the remaining characters are added as the 
    last element of the returned list.

    >>> split_strings('HelloWorld', 3)
    ['Hel', 'loW', 'orl', 'd']
    >>> split_strings('CodingIsFun', 5)
    ['Codin', 'gIsFu', 'n']
    """
    return [s[i:i + n] for i in range(0, len(s), n)]