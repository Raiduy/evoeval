def letter_shift_cipher(s, n):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    vowel_count = 0
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted += alphabet[(alphabet.index(char) + n) % 26]
            else:
                encrypted += alphabet[(alphabet.index(char.lower()) + n) % 26].upper()
            if char.lower() in vowels:
                vowel_count += 1
        else:
            encrypted += char
    return (encrypted, vowel_count)