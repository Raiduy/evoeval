
def shifted_upper_count(s, shift):
    if shift > len(s):
        s = s[::-1]
    else:
        s = s[-shift:] + s[:-shift]
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            count += 1
    return count