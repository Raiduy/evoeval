
from typing import List, Tuple

def sort_and_pluck(values: List[str]) -> Tuple[str, int]:
    numeral_to_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    number_to_numeral = {v: k for (k, v) in numeral_to_number.items()}
    sorted_values = []
    for value in values:
        sorted_numerals = sorted(value.split(), key=lambda x: numeral_to_number[x])
        sorted_values.append(sorted_numerals)
    smallest_even = None
    original_index = None
    for (index, sorted_numerals) in enumerate(sorted_values):
        for numeral in sorted_numerals:
            number = numeral_to_number[numeral]
            if number % 2 == 0:
                if smallest_even is None or number < numeral_to_number[smallest_even]:
                    smallest_even = numeral
                    original_index = index
                break
    if smallest_even is not None:
        return (smallest_even, original_index)
    else:
        return ()