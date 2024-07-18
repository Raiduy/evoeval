
def encrypt(s):
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + 4) % 26 + 97)
            if char.isupper():
                encrypted_string += shifted_char.upper()
            else:
                encrypted_string += shifted_char
        else:
            encrypted_string += char
    return encrypted_string