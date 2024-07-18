
from typing import List, Tuple

def sort_and_pluck(values: List[str]) -> Tuple[str, int]:
    numerals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    even_numerals = ['zero', 'two', 'four', 'six', 'eight']
    result = []
    for (i, value) in enumerate(values):
        sorted_value = sorted(value.split(), key=lambda x: numerals.index(x))
        for numeral in sorted_value:
            if numeral in even_numerals:
                result.append((numeral, i))
                break
    if not result:
        return ()
    else:
        return min(result, key=lambda x: (even_numerals.index(x[0]), x[1]))