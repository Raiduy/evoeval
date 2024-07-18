
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters and the same length.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    False
    >>> same_chars('aaaaaaabcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    False
    >>> same_chars('eabcd', 'ddabc')
    False
    """
    return sorted(s0) == sorted(s1) and len(s0) == len(s1)