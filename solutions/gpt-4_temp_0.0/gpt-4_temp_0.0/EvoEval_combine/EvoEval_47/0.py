def count_odd_upper(s, lst):
    vowels = 'AEIOU'
    n = sum((1 for i in range(0, len(s), 2) if s[i] in vowels))
    result = []
    for string in lst:
        m = sum((1 for digit in string if int(digit) % 2 != 0))
        result.append(f'In the string, the number of uppercase vowels in even indices is {n}, and the number of odd digits is {m}.')
    return result