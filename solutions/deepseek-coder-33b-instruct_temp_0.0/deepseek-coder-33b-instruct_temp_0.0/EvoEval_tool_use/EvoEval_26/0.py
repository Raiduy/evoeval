def is_valid_string(input_string: str) -> bool:
    """
    Check if a string is valid. A string is valid if it only contains alphanumeric characters (letters and numbers).
    Returns True if the string is valid, False otherwise.
    """
    return input_string.isalnum()
from typing import List

def transform_strings(strings: List[str]) -> List[str]:
    """
    Given a list of strings, transform each string into a new one according to the following rules:
    - If the string is valid (only contains alphanumeric characters), reverse the string.
    - If the string is not valid, replace each non-alphanumeric character with a hyphen '-'.
    Return the list of transformed strings, keeping the original order.
    >>> transform_strings(['abc', 'a#b', '123'])
    ['cba', 'b-a', '321']
    """
    transformed_strings = []
    for string in strings:
        if is_valid_string(string):
            transformed_strings.append(string[::-1])
        else:
            transformed_string = ''
            for char in string:
                if not char.isalnum():
                    transformed_string += '-'
                else:
                    transformed_string += char
            transformed_strings.append(transformed_string)
    return transformed_strings