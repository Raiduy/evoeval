import hashlib

def mini_roman_to_md5(number):
    if number <= 0:
        return None
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    roman = ''
    for i in range(len(values)):
        count = int(number / values[i])
        roman += numerals[i] * count
        number -= values[i] * count
    md5_hash = hashlib.md5()
    md5_hash.update(roman.encode())
    return md5_hash.hexdigest()