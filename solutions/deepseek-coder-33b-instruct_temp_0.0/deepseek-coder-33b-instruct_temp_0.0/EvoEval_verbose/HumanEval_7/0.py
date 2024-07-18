from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ 
    This function takes in two parameters, a list of strings named 'strings' and a string named 'substring'. 
    Its main purpose is to filter the input 'strings' list by only including those strings that contain the provided 'substring'. 

    The function iteratively checks each string in the 'strings' list. If it finds that the 'substring' is present in a string, 
    it includes that string in the resulting output list. If not, it simply moves on to the next string in the list.

    The function finally returns a list of strings which is a subset of the original 'strings' input list, 
    consisting only of those strings that contain the specified 'substring'.

    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring to be searched for within the strings of the list.

    Returns:
    List[str]: A list of strings from the input 'strings' list that contain the specified 'substring'.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]