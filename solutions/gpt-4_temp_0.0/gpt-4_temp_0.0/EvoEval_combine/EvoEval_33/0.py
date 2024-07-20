
def roman_happiness(s):
    """
    Given a string s of Roman numerals in lowercase, your task is to check if the roman numeral string is happy or not.

    Definition:
    A Roman numeral string is happy if:
    1. Its length is at least 3.
    2. It represents a positive integer less than or equal to 1000.
    3. Every 3 consecutive letters are distinct.

    If the string does not meet the criteria, return False. If the string is happy, return the integer that it represents.

    For example:
    roman_happiness('i') => False
    roman_happiness('ii') => False
    roman_happiness('xiv') => 14
    roman_happiness('iiv') => False
    roman_happiness('xiv') => 14
    roman_happiness('xxxi') => False
    roman_happiness('xliv') => 44
    """
    roman_to_int = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    int_val = 0
    prev = 0
    for i in range(len(s)):
        curr = roman_to_int[s[i]]
        if curr > prev:
            int_val += curr - 2 * prev
        else:
            int_val += curr
        prev = curr
    if len(s) < 3 or int_val > 1000:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return int_val