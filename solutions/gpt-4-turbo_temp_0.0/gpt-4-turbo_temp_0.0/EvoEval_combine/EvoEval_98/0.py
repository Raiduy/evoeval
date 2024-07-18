
def check_dict_bracketing(dict):
    if not dict:
        return False
    all_lower = all((key.islower() for key in dict.keys()))
    all_upper = all((key.isupper() for key in dict.keys()))
    if not (all_lower or all_upper):
        return False

    def is_correct_bracketing(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    for value in dict.values():
        if not is_correct_bracketing(value):
            return False
    return True