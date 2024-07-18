def count_odd_upper(s, lst):
    vowels = ['A', 'E', 'I', 'O', 'U']
    n = sum((1 for i in range(len(s)) if i % 2 == 0 and s[i] in vowels))
    result = []
    for string in lst:
        m = sum((1 for char in string if int(char) % 2 != 0))
        result.append(f'In the string, the number of uppercase vowels in even indices is {n}, and the number of odd digits is {m}.')
    return result