def vowels_count(s):
    vowels = 'aeiou'
    s = s.lower()
    count = sum((1 for char in s if char in vowels))
    if s[-1] == 'y':
        count += 1
    return count