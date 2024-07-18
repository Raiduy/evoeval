
from typing import List

def roman_prefixes(number: int) -> List[str]:

    def int_to_roman(input):
        if not 0 < input < 4000:
            raise ValueError('Argument must be between 1 and 3999')
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i')
        result = []
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count
        return ''.join(result)
    roman_number = int_to_roman(number)
    prefixes = [roman_number[:i] for i in range(len(roman_number) + 1)]
    return prefixes