
from typing import List

def sort_parentheses(lst: List[str]) -> str:
    string = ''.join(lst)
    open_parentheses = 0
    for char in string:
        if char == '(':
            open_parentheses += 1
        elif char == ')':
            open_parentheses -= 1
        if open_parentheses < 0:
            return 'No'
    if open_parentheses != 0:
        return 'No'
    return 'Yes'