
from typing import List

def roman_prefixes(number: int) -> List[str]:
    roman_num = int_to_roman(number)
    return [roman_num[:i] for i in range(1, len(roman_num) + 1)]