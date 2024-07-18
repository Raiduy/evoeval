
from typing import List, Tuple

def sort_and_pluck(values: List[str]) -> Tuple[str, int]:
    even_numerals = []
    for (i, value) in enumerate(values):
        numerals = value.split()
        numerals.sort()
        for numeral in numerals:
            if numeral in ['zero', 'two', 'four', 'six', 'eight']:
                even_numerals.append((numeral, i))
    if not even_numerals:
        return ()
    even_numerals.sort(key=lambda x: (int(x[0][0]) % 2, x[1]))
    return even_numerals[0]