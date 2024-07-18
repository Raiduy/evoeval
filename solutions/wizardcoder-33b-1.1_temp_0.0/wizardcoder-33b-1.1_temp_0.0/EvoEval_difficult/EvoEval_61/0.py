def correct_bracketing_advanced(brackets: str):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    for bracket in brackets:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs.keys():
            if stack == [] or bracket_pairs[bracket] != stack.pop():
                return False
    return stack == []