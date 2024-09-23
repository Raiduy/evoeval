
from typing import List

def roman_prefixes(number: int) -> List[str]:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string in lowercase.
    Afterwards, return a list of all prefixes of the roman numeral from shortest to longest.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> roman_prefixes(19) == ['x', 'xi', 'xix']
    >>> roman_prefixes(152) == ['c', 'cl', 'cli', 'clii']
    >>> roman_prefixes(426) == ['c', 'cd', 'cdx', 'cdxx', 'cdxxv', 'cdxxvi']
    """
    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    keys = sorted(roman_numerals.keys(), reverse=True)
    roman_string = ''
    for key in keys:
        while number >= key:
            roman_string += roman_numerals[key]
            number -= key
    return [roman_string[:i + 1] for i in range(len(roman_string))]