
def roman_happiness(s):
    if len(s) < 3:
        return False
    integer_value = roman_to_int(s)
    if integer_value > 1000:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) < 3:
            return False
    return integer_value