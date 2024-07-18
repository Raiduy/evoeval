from typing import List, Tuple

def interleave_and_concatenate(strings: List[str], integers: List[int]) -> Tuple[str, int]:
    interleaved = [val for pair in zip(strings, integers) for val in pair]
    interleaved_strings = [val for val in interleaved if isinstance(val, str)]
    interleaved_integers = [val for val in interleaved if isinstance(val, int)]
    concatenated_string = ''.join(interleaved_strings)
    sum_integers = sum(interleaved_integers)
    return (concatenated_string, sum_integers)