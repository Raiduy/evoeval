
def check_dict_bracketing(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    values = list(dict.values())
    if not all((key.islower() for key in keys)) and (not all((key.isupper() for key in keys))):
        return False
    if not all((value.count('(') == value.count(')') for value in values)):
        return False
    stack = []
    for value in values:
        for char in value:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
    if stack:
        return False
    return True