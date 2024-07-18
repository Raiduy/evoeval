from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    This function takes in a string as an argument and then returns a list of all possible prefixes of the input string. 
    The prefixes are returned in ascending order of their length, i.e., from the shortest prefix to the longest one. 

    A prefix of a string is defined as any leading contiguous part of the string. For example, 'a', 'ab', and 'abc' 
    are all prefixes of the string 'abc'. In the context of this function, the shortest prefix is a single-character 
    string that consists of the first character of the input string, and the longest prefix is the input string itself.

    The function uses the following inputs and outputs:

    Inputs:
    - A string (of any length, including an empty string)

    Outputs:
    - A list of strings, where each string is a prefix of the input string. The list is sorted in order of increasing 
      prefix length.

    Example:
    If the function is called with the input string 'abc', it returns the list ['a', 'ab', 'abc']
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]