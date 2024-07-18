from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    This function is designed to filter a list of input strings based on a provided prefix.
    The function takes two arguments: a list of strings and a prefix string.
    
    The function will iterate through each string in the provided list and checks if that string begins with the specified prefix. 
    If a string starts with the given prefix, it will be included in the output list. If it does not start with the prefix, it will be excluded.
    
    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix the function will check for at the start of each string in the 'strings' list.

    Returns:
        List[str]: A list of strings from the input 'strings' list that start with the provided 'prefix'.

    Examples:
        An empty input list will return an empty list, regardless of the provided prefix:
        >>> filter_by_prefix([], 'a')
        []

        For a list containing 'abc', 'bcd', 'cde', 'array', and a prefix of 'a', the function will return ['abc', 'array'], 
        as these are the only strings in the list that start with 'a':
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]