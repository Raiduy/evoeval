
def check_dict_bracketing(dict):
    """
    Given a dictionary where all keys and values are strings, return True if all keys and values 
    follow these two rules, else return False. The function should return False if the given
    dictionary is empty. 

    Rule 1: All keys are strings in lower case or all keys are strings in upper case.
    Rule 2: All values are strings of "(" and ")" and have correct bracketing - every opening 
    bracket has a corresponding closing bracket.

    Examples:
    check_dict_bracketing({"a":"()", "b":"(())"}) should return True.
    check_dict_bracketing({"a":"()", "A":"()"}) should return False.
    check_dict_bracketing({"a":"(", "b":"()"}) should return False.
    check_dict_bracketing({"Name":"()", "Age":"(())"}) should return False.
    check_dict_bracketing({"STATE":"()", "ZIP":"(())"}) should return True.
    """
    if not dict:
        return False
    keys = list(dict.keys())
    values = list(dict.values())
    if not (all((key.islower() for key in keys)) or all((key.isupper() for key in keys))):
        return False
    for value in values:
        stack = []
        for char in value:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        if stack:
            return False
    return True