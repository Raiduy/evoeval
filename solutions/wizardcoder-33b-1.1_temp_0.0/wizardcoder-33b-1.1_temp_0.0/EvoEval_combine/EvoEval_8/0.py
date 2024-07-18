
def correct_bracket_sequence_and_count(string: str, bracket: str) -> tuple:
    count = 0
    stack = []
    for char in string:
        if char == bracket:
            count += 1
            stack.append(char)
        elif stack:
            stack.pop()
        else:
            return (False, count)
    return (not stack, count)