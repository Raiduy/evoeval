def correct_bracketing_advanced(brackets: str) -> bool:
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for bracket in brackets:
        if bracket in bracket_pairs:
            stack.append(bracket)
        elif not stack or bracket_pairs[stack.pop()] != bracket:
            return False
    return not stack