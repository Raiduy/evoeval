def vowels_count(s, l=None):
    vowels = 'aeiou' if l is None else ''.join(l).lower()
    s = s.lower()
    count = sum((1 for char in s if char in vowels))
    if 'y' in s[-1] if l is None else 'y' in s[-1] if 'y' in vowels else False:
        count += 1
    return count