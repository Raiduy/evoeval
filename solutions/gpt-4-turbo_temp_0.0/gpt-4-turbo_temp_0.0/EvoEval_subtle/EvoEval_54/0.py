
def same_chars(s0: str, s1: str) -> bool:
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
    if len(s0) != len(s1):
        return False
    from collections import Counter
    return Counter(s0) == Counter(s1)