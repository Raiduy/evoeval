def count_odd_upper(s, lst):
    vowels = 'AEIOU'
    n = sum((1 for i in range(len(s)) if i % 2 == 0 and s[i] in vowels))
    result = []
    for string in lst:
        m = sum((1 for digit in string if int(digit) % 2 != 0))
        result.append('In the string, the number of uppercase vowels in even indices is {}, and the number of odd digits is {}.'.format(n, m))
    return result