from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ 
    This function takes a list of strings as an argument. The objective is to find and return 
    the longest string from the list. In the event of a tie (i.e., multiple strings have the 
    same maximum length), the function will return the first longest string encountered. 

    If the input list is empty, the function returns None.

    Args:
    strings (List[str]): A list of strings from which the longest string will be selected.

    Returns:
    Optional[str]: The longest string present in the input list. If multiple strings share the 
    longest length, the first such string is returned. If the input list is empty, None is returned.

    Examples:
    
    An empty list returns None:
    >>> longest([])
    None
    
    A list with strings of the same length returns the first string:
    >>> longest(['a', 'b', 'c'])
    'a'
    
    A list with strings of varying lengths returns the longest string:
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'

    """
    if not strings:
        return None
    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string