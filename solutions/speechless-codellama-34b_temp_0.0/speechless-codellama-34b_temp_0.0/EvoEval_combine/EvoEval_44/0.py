
from typing import List

def roman_prefixes(number: int) -> List[str]:
    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    roman_prefixes = []
    roman_num = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while number >= value:
            roman_num += roman_numerals[value]
            number -= value
    for i in range(len(roman_num)):
        roman_prefixes.append(roman_num[:i + 1])
    return roman_prefixes