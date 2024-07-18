from typing import List, Tuple, Union

def check_validity(input: Union[str, List[str]]) -> Union[bool, List[bool]]:
    """ This helper function checks if a string is alphanumeric (made up of only letters and numbers) or 
    in case of a list of strings, return a list of booleans indicating whether each string is alphanumeric.

    >>> check_validity('abc123')
    True
    >>> check_validity('abc@123')
    False
    >>> check_validity(['abc123', 'abc@123'])
    [True, False]
    """
    if isinstance(input, str):
        return input.isalnum()
    elif isinstance(input, list):
        return [s.isalnum() for s in input]
from typing import List, Tuple

def get_valid_and_invalid_strings(strings: List[str]) -> Tuple[List[str], List[str]]:
    valid_strings = [s for s in strings if s.isalnum()]
    invalid_strings = [s for s in strings if not s.isalnum()]
    return (valid_strings, invalid_strings)