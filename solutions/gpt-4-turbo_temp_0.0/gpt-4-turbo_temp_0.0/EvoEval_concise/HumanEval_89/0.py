
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rotated_char = chr(base + (ord(char) - base + 4) % 26)
            result += rotated_char
        else:
            result += char
    return result