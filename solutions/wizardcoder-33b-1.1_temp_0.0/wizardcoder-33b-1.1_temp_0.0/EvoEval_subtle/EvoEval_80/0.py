
def is_happy(s):
    if len(s) < 4:
        return False
    for i in range(len(s) - 3):
        if len(set(s[i:i + 4])) != 4:
            return False
    return True