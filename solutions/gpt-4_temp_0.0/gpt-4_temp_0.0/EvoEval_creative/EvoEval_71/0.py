def letter_shift_cipher(s, n):
    vowels = 'aeiou'
    result = ''
    vowel_count = 0
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + n) % 26 + ascii_offset)
            result += shifted_char
            if shifted_char.lower() in vowels:
                vowel_count += 1
        else:
            result += char
    return (result, vowel_count)