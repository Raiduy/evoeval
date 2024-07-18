def letter_shift_cipher(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encrypted_string = ''
    vowel_count = 0
    for char in s:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + n) % 26 + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_string += shifted_char
            if shifted_char.lower() in vowels:
                vowel_count += 1
        else:
            encrypted_string += char
    return (encrypted_string, vowel_count)