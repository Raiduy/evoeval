from typing import List, Tuple

def interleave_and_concatenate(strings: List[str], integers: List[int]) -> Tuple[str, int]:
    result_string = ''
    result_integer = 0
    max_length = max(len(strings), len(integers))
    for i in range(max_length):
        if i < len(strings):
            result_string += strings[i]
        if i < len(integers):
            result_integer += integers[i]
    return (result_string, result_integer)