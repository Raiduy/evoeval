def correct_bracketing_advanced(brackets: str):
    stack = []
    opening_brackets = '({['
    closing_brackets = ')}]'
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[bracket]:
                return False
            stack.pop()
    return not stack