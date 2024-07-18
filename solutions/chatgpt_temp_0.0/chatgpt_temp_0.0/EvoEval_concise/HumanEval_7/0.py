from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Returns list of input strings containing the specified substring.

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)
    return filtered_strings