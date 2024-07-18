import hashlib

def mini_roman_to_md5(number):
    """
    Given a positive integer 'number', convert it to its roman numeral equivalent as a string in lowercase.
    Return the md5 hash of the roman numeral string. If 'number' is zero or negative, return None.
    Restrictions: 0 <= num <= 1000
    """
    if number <= 0:
        return None
    roman_numeral = int_to_roman(number)
    md5_hash = hashlib.md5(roman_numeral.encode()).hexdigest()
    return md5_hash