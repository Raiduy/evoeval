from typing import List, Tuple

def parse_nested_parens(paren_string: str) -> List[Tuple[str, int]]:
    groups = paren_string.split()
    result = []
    for group in groups:
        stack = []
        max_depth = {'()': 0, '[]': 0, '{}': 0}
        cur_depth = 0
        for char in group:
            if char in '([{':
                stack.append(char)
                cur_depth += 1
                if cur_depth > max_depth[stack[-1] + stack[-2]]:
                    max_depth[stack[-1] + stack[-2]] = cur_depth
            elif char in ')]}':
                cur_depth -= 1
                stack.pop()
        result.append((group, {k: v for (k, v) in max_depth.items() if v > 0}))
    return result