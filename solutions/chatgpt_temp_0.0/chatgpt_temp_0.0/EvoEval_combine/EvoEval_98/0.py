
def check_dict_bracketing(dict):
    if len(dict) == 0:
        return False
    keys = list(dict.keys())
    first_key = keys[0]
    is_lower_case = first_key.islower()
    is_upper_case = first_key.isupper()
    for key in keys:
        if is_lower_case and (not key.islower()) or (is_upper_case and (not key.isupper())):
            return False
        value = dict[key]
        if not all((c in '()[]' for c in value)):
            return False
        stack = []
        for c in value:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
    return True