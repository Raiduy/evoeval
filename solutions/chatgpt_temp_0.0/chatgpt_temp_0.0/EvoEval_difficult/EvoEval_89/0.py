def advanced_encrypt(s, n):
    encrypted = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - 97 + n * 2) % 26 + 97)
            else:
                encrypted += chr((ord(char) - 65 + n * 2) % 26 + 65)
        else:
            encrypted += char
    return encrypted