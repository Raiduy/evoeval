
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        else:
            if len(stack) == 0 or stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) > 0

