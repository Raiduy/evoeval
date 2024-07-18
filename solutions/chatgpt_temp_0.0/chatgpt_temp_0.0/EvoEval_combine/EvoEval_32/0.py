
from typing import List

def circular_shift_nested_parens(input: List[str], shift: int) -> List[int]:
    depths = []
    for group in input:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        depths.append(max_depth)
    num = int(''.join(map(str, depths)))
    num_str = str(num)
    if shift > len(num_str):
        shifted_num_str = num_str[::-1]
    else:
        shifted_num_str = num_str[-shift:] + num_str[:-shift]
    shifted_num = int(shifted_num_str)
    shifted_digits = [int(digit) for digit in str(shifted_num)]
    return shifted_digits