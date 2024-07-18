def letter_shift_cipher(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    encrypted_string = ''
    vowel_count = 0
    for char in s:
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) + n) % 26
            encrypted_char = alphabet[index]
            encrypted_string += encrypted_char
            if encrypted_char.lower() in vowels:
                vowel_count += 1
        else:
            encrypted_string += char
    return (encrypted_string, vowel_count)