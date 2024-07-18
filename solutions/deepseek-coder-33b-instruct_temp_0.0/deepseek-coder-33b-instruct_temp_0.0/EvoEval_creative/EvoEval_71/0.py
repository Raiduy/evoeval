def letter_shift_cipher(s, n):
    vowels = 'aeiou'
    vowel_count = 0
    result = ''
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - ascii_offset + n) % 26 + ascii_offset)
            result += new_char
            if new_char.lower() in vowels:
                vowel_count += 1
        else:
            result += char
    return (result, vowel_count)