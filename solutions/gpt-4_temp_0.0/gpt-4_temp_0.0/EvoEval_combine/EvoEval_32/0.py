
from typing import List

def circular_shift_nested_parens(input: List[str], shift: int) -> List[int]:
    """ 
    The input to this function is a list of strings. Each string represents multiple groups for nested parentheses 
    separated by spaces. For each group, calculate the deepest level of nesting of parentheses.
    
    After that, concatenate the list of nesting depths as a single number and apply a circular shift on that number. Shift 
    the digits of the number right by the provided shift value. If shift > number of digits, return digits reversed.
    
    Return the result as a list of individual digits after the circular shift.

    >>> circular_shift_nested_parens(['(()())', '((()))', '()', '((())()())'], 2)
    [1, 3, 2, 3]
    >>> circular_shift_nested_parens(['(()())', '((()))', '()', '((())()())'], 1)
    [3, 2, 3, 1]
    """
    nesting_depths = []
    for group in input:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        nesting_depths.append(max_depth)
    number = int(''.join(map(str, nesting_depths)))
    number_str = str(number)
    if shift > len(number_str):
        result = list(map(int, reversed(number_str)))
    else:
        result = list(map(int, number_str[-shift:] + number_str[:-shift]))
    return result