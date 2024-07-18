from typing import List, Tuple

def parse_nested_parens(paren_string: str) -> List[Tuple[str, dict]]:
    groups = paren_string.split()
    result = []
    for group in groups:
        max_levels = {}
        current_level = 0
        for char in group:
            if char in ['(', '[', '{']:
                current_level += 1
                if char in max_levels:
                    max_levels[char] = max(max_levels[char], current_level)
                else:
                    max_levels[char] = current_level
            elif char in [')', ']', '}']:
                current_level -= 1
        result.append((group, max_levels))
    return result