def correct_bracketing_advanced(brackets: str, scope: tuple):
    stack = []
    bracket_pairs = {'<': '>', '[': ']', '{': '}', '(': ')'}
    for bracket in brackets:
        if bracket in bracket_pairs.values() and stack and (bracket_pairs[stack[-1]] == bracket):
            stack.pop()
        elif bracket in bracket_pairs.keys() and bracket in scope:
            stack.append(bracket)
        elif bracket in bracket_pairs.values() and bracket not in scope:
            return False
    return not stack