import hashlib

def mini_roman_to_md5(number):
    """
    Given a positive integer 'number', convert it to its roman numeral equivalent as a string in lowercase.
    Return the md5 hash of the roman numeral string. If 'number' is zero or negative, return None.
    Restrictions: 0 <= num <= 1000

    Examples:
    >>> mini_roman_to_md5(19) == 'deecbfa00b6b28500a8a2b0d2cd484f2'
    >>> mini_roman_to_md5(152) == 'e63c5e3bfe23f38e0550b1aa0602d67b'
    >>> mini_roman_to_md5(426) == '47863739f1551f4cfb83b7d0101a1d0b'
    """
    if number <= 0:
        return None
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    roman_num = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return hashlib.md5(roman_num.encode()).hexdigest()