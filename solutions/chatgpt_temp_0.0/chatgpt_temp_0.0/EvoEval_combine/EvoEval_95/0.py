
from typing import List

def filter_sort_strings(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given substring and have an even length. 
    Return the resulted list in ascending order by the length of each word. 
    If two words have the same length, sort the list alphabetically.
    The list may contain duplicate strings.
    
    For example:
    >>> filter_sort_strings([], 'a')
    []
    >>> filter_sort_strings(['abc', 'bacd', 'cd', 'array'], 'a')
    ['bacd']
    >>> filter_sort_strings(['abc', 'bacd', 'cd', 'array', 'play'], 'a')
    ['bacd', 'play']
    """
    filtered_strings = [s for s in strings if substring in s and len(s) % 2 == 0]
    sorted_strings = sorted(filtered_strings, key=lambda x: (len(x), x))
    return sorted_strings