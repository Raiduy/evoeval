
def encrypt(s):
    encrypted = ''
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            shifted_val = ascii_val + 2 * 2
            if char.isupper():
                if shifted_val > ord('Z'):
                    shifted_val -= 26
                encrypted += chr(shifted_val)
            else:
                if shifted_val > ord('z'):
                    shifted_val -= 26
                encrypted += chr(shifted_val)
        else:
            encrypted += char
    return encrypted