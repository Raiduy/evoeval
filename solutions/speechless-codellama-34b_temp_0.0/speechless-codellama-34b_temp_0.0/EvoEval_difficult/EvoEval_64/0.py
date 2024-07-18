def vowels_count(s, l=None):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if l is not None:
        vowels = l
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            if s[i] == 'y' and i != len(s) - 1:
                continue
            count += 1
    return count