
from typing import List, Tuple

def sort_and_pluck(values: List[str]) -> Tuple[str, int]:
    numeral_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    min_even_value = float('inf')
    min_even_index = float('inf')
    min_even_numeral = ''
    for (i, value) in enumerate(values):
        nums = value.split()
        nums.sort(key=lambda x: numeral_map[x])
        for (j, num) in enumerate(nums):
            if numeral_map[num] % 2 == 0 and numeral_map[num] < min_even_value:
                min_even_value = numeral_map[num]
                min_even_index = j
                min_even_numeral = num
    return (min_even_numeral, min_even_index) if min_even_numeral else ()