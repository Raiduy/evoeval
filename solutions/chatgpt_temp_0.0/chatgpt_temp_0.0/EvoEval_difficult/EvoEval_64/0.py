def vowels_count(s, l=None):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if l:
        vowels = l
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] in vowels:
            if s[i] == 'y':
                if i == len(s) - 1 or s[i + 1] not in vowels:
                    count += 1
            else:
                count += 1
    return count