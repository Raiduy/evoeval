def count_odd_upper(s, lst):
    n = sum((1 for i in range(0, len(s), 2) if s[i] in 'AEIOU'))
    return [f'In the string, the number of uppercase vowels in even indices is {n}, and the number of odd digits is {sum((int(c) % 2 for c in s))}.' for s in lst]