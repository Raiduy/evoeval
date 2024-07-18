def count_odd_upper(s, lst):
    vowels = set('AEIOU')
    result = []

    def count_vowels(s):
        return sum((1 for (i, c) in enumerate(s) if c.upper() in vowels and i % 2 == 0))

    def count_odd_digits(s):
        return sum((1 for c in s if int(c) % 2 != 0))
    n = count_vowels(s)
    for string in lst:
        m = count_odd_digits(string)
        result.append(f'In the string, the number of uppercase vowels in even indices is {n}, and the number of odd digits is {m}.')
    return result