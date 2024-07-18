from typing import List, Tuple

def parse_nested_parens(paren_string: str) -> List[Tuple[str, int]]:

    def get_deepest_level(paren_str: str) -> int:
        stack = []
        max_levels = {}
        current_level = 0
        for char in paren_str:
            if char in '([{':
                current_level += 1
                max_levels[char] = max(max_levels.get(char, 0), current_level)
                stack.append(char)
            elif char in ')]}':
                current_level -= 1
                stack.pop()
        return max_levels
    groups = paren_string.split()
    result = []
    for group in groups:
        paren_dict = get_deepest_level(group)
        result.append((group, paren_dict))
    return result