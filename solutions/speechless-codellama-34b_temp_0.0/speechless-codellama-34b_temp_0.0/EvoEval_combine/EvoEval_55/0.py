import hashlib

def mini_roman_to_md5(number):
    if number <= 0:
        return None
    roman_numerals = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}
    roman_string = ''
    for (value, numeral) in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            roman_string += numeral
            number -= value
    md5_hash = hashlib.md5(roman_string.encode()).hexdigest()
    return md5_hash