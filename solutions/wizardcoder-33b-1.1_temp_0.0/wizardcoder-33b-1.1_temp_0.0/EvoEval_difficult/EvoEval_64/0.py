def vowels_count(s, l=None):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if l is not None:
        vowels = [v.lower() for v in l]
    s = s.lower()
    count = 0
    for char in s:
        if char in vowels:
            count += 1
        elif char == 'y' and s.index(char) == len(s) - 1:
            count += 1
    return count