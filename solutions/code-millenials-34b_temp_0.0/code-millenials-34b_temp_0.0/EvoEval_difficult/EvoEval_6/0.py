from typing import List, Tuple

def parse_nested_parens(paren_string: str) -> List[Tuple[str, Dict[str, int]]]:
    result = []
    groups = paren_string.split()
    for group in groups:
        max_depths = {}
        current_depth = 0
        current_char = None
        for char in group:
            if char in ['(', '{', '[']:
                if current_depth == 0:
                    current_char = char
                current_depth += 1
            elif char in [')', '}', ']']:
                current_depth -= 1
                if current_depth == 0:
                    if current_char in max_depths:
                        max_depths[current_char] = max(max_depths[current_char], current_depth + 1)
                    else:
                        max_depths[current_char] = current_depth + 1
        result.append((group, max_depths))
    return result