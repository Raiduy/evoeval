
from typing import List

def sort_parentheses(lst: List[str]) -> str:
    num_count = {str(i): 0 for i in range(10)}
    for s in lst:
        for c in s:
            if c.isdigit():
                num_count[c] += 1
    stack = []
    for s in sorted(lst, key=lambda x: [num_count[c] for c in x if c.isdigit()]):
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return 'No'
                stack.pop()
    return 'Yes' if not stack else 'No'