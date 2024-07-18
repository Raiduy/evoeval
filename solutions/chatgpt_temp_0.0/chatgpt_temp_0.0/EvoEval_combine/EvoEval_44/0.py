
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
    roman_numerals = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}

    def to_roman(num: int) -> str:
        result = ''
        for (value, symbol) in roman_numerals.items():
            while num >= value:
                result += symbol
                num -= value
        return result
    roman_numeral = to_roman(number)
    prefixes = [roman_numeral[:i] for i in range(1, len(roman_numeral) + 1)]
    return prefixes