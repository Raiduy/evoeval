from typing import List, Tuple

def parse_nested_parens(paren_string: str) -> List[Tuple[str, int]]:

    def max_depth(s: str) -> dict:
        depth = {'(': 0, '[': 0, '{': 0}
        max_depth = {'()': 0, '[]': 0, '{}': 0}
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
                depth[char] += 1
                if char == '(':
                    max_depth['()'] = max(max_depth['()'], depth[char])
                elif char == '[':
                    max_depth['[]'] = max(max_depth['[]'], depth[char])
                elif char == '{':
                    max_depth['{}'] = max(max_depth['{}'], depth[char])
            elif char in ')]}':
                if char == ')' and stack and (stack[-1] == '('):
                    depth['('] -= 1
                    stack.pop()
                elif char == ']' and stack and (stack[-1] == '['):
                    depth['['] -= 1
                    stack.pop()
                elif char == '}' and stack and (stack[-1] == '{'):
                    depth['{'] -= 1
                    stack.pop()
        return {k: v for (k, v) in max_depth.items() if v > 0}
    groups = paren_string.split()
    result = []
    for group in groups:
        result.append((group, max_depth(group)))
    return result