
def encrypt(s):
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            shift = 4
            if char.islower():
                encrypted_string += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_string += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_string += char
    return encrypted_string