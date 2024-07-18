
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
    if len(s) < 3:
        return False
    roman_values = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    total = 0
    prev = None
    count = 0
    for letter in s:
        if letter not in roman_values:
            return False
        value = roman_values[letter]
        if prev is not None and prev == letter:
            count += 1
            if count >= 3:
                return False
        else:
            count = 1
        total += value
        prev = letter
    if total > 1000:
        return False
    return total