
def solve_and_count(s):
    vowels = 'AEIOUaeiou'
    uppercase_vowels = 'AEIOU'
    has_letters = any((c.isalpha() for c in s))
    if has_letters:
        result_string = ''.join((c.swapcase() if c.isalpha() else c for c in s))
    else:
        result_string = s[::-1]
    count_uppercase_vowels_even = sum((1 for (i, c) in enumerate(result_string) if i % 2 == 0 and c in uppercase_vowels))
    return (result_string, count_uppercase_vowels_even)