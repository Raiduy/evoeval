def vowels_count(s, l=None):
    s = s.lower()
    if l is not None:
        custom_vowels = [vowel.lower() for vowel in l]
    else:
        custom_vowels = ['a', 'e', 'i', 'o', 'u']
        if s.endswith('y'):
            custom_vowels.append('y')
    count = sum((1 for char in s if char in custom_vowels))
    return count