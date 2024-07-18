def count_odd_upper(s, lst):
    uppercase_vowels = 'AEIOU'
    n = sum((1 for i in range(0, len(s), 2) if s[i] in uppercase_vowels))
    output = []
    for string in lst:
        m = sum((1 for char in string if int(char) % 2 != 0))
        output.append(f'In the string, the number of uppercase vowels in even indices is {n}, and the number of odd digits is {m}.')
    return output