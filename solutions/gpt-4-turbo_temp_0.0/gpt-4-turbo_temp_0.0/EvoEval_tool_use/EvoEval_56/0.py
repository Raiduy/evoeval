def find_subsequence_index(original: str, target: str):
    """
    original and target are strings. 
    This function finds the starting index of the target string in the original string and returns it. If the target is not present, it returns -1.

    >>> find_subsequence_index("Hello world", "world")
    6
    >>> find_subsequence_index("abcdefg", "cd")
    2
    >>> find_subsequence_index("aaa", "a")
    0
    >>> find_subsequence_index("Hello world", "Hello")
    0
    """
    return original.find(target)
def replace_subsequence(original: str, target: str, replacement: str) -> str:
    """
    original, target, and replacement are strings. 
    The function replaces all occurrences of the target subsequence in the original string with the replacement string. 
    The function should be case sensitive.
    If there are no occurrences of the target, return 'no occurrence'.

    >>> replace_subsequence("Hello world", "world", "Earth")
    "Hello Earth"
    >>> replace_subsequence("abcdefg", "cd", "1234")
    "ab1234efg"
    >>> replace_subsequence("aaa", "a", "b")
    "bbb"
    >>> replace_subsequence("Hello world", "Hello", "Hi")
    "Hi world"
    """
    replaced_string = original.replace(target, replacement)
    if replaced_string == original:
        return 'no occurrence'
    else:
        return replaced_string