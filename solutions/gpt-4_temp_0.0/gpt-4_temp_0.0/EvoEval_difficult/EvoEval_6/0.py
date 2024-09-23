from typing import List, Tuple

def parse_nested_parens(paren_string: str) -> List[Tuple[str, int]]:
    paren_types = ['()', '[]', '{}']
    groups = paren_string.split()
    result = []
    for group in groups:
        paren_depths = {pt: 0 for pt in paren_types}
        current_depths = {pt: 0 for pt in paren_types}
        for char in group:
            for pt in paren_types:
                if char == pt[0]:
                    current_depths[pt] += 1
                    paren_depths[pt] = max(paren_depths[pt], current_depths[pt])
                elif char == pt[1]:
                    current_depths[pt] -= 1
        paren_depths = {pt: depth for (pt, depth) in paren_depths.items() if depth > 0}
        result.append((group, paren_depths))
    return result