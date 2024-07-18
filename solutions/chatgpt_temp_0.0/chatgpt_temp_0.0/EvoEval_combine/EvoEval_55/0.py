import hashlib

def mini_roman_to_md5(number):
    if number <= 0:
        return None
    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    result = ''
    for (value, numeral) in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while number >= value:
            result += numeral
            number -= value
    md5_hash = hashlib.md5(result.encode()).hexdigest()
    return md5_hash