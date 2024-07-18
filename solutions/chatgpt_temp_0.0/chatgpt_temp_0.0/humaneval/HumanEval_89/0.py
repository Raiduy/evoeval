
def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            if char.islower():
                encrypted += chr((ascii_val - 97 + 2 * 2) % 26 + 97)
            else:
                encrypted += chr((ascii_val - 65 + 2 * 2) % 26 + 65)
        else:
            encrypted += char
    return encrypted
