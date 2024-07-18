
def shifted_upper_count(s, shift):
    uppercase_vowels = 'AEIOU'
    if shift > len(s):
        s = s[::-1]
    shifted_s = ''
    for char in s:
        shifted_char = chr((ord(char) + shift) % 128)
        shifted_s += shifted_char
    count = 0
    for i in range(0, len(shifted_s), 2):
        if shifted_s[i] in uppercase_vowels:
            count += 1
    return count