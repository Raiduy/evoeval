from typing import List, Tuple

def helper_function1(s: str) -> Tuple[str, int]:
    """ 
    Process a string and return a tuple containing the string in reverse order and its length.

    :param s: input string
    :return: a tuple of the reversed string and string length

    >>> helper_function1('hello')
    ('olleh', 5)
    """
    return s[::-1], len(s)


def helper_function2(s: str) -> bool:
    """ 
    Check if a string is a palindrome.

    :param s: input string
    :return: True if the string is a palindrome, False otherwise

    >>> helper_function2('radar')
    True

    >>> helper_function2('hello')
    False
    """
    return s == s[::-1]
def process_strings(string_list: List[str]) -> List[Tuple[str, str, int, bool]]:
    """ 
    The function takes in a list of strings. 
    
    It returns a list of tuples. Each tuple contains the original string in string_list, its reverse, its 
    length and a boolean indicating whether the reversed string is a palindrome or not.

    >>> process_strings(['hello', 'radar', 'world'])
    [('hello', 'olleh', 5, False), ('radar', 'radar', 5, True), ('world', 'dlrow', 5, False)]
    """
    result = []
    for s in string_list:
        (reverse, length) = helper_function1(s)
        palindrome = helper_function2(reverse)
        result.append((s, reverse, length, palindrome))
    return result