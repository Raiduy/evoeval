
def match_parens(lst):
    concatenated_string = lst[0] + lst[1]
    stack = []
    for char in concatenated_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    if len(stack) > 0:
        return 'No'
    else:
        return 'Yes'