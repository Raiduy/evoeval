
from typing import List

def roman_prefixes(number: int) -> List[str]:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string in lowercase.
    Afterwards, return a list of all prefixes of the roman numeral from shortest to longest.
    """
    roman_numeral = int_to_roman(number)
    prefixes = [roman_numeral[:i] for i in range(1, len(roman_numeral) + 1)]
    return prefixes