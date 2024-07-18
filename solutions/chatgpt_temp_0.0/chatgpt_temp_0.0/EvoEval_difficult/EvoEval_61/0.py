def correct_bracketing_advanced(brackets: str):
    stack = []
    opening_brackets = '({['
    closing_brackets = ')}]'
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != bracket:
                return False
    return len(stack) == 0