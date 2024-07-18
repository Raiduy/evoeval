
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            if ascii_val >= 65 and ascii_val <= 90:
                result += chr((ascii_val - 65 + 4) % 26 + 65)
            elif ascii_val >= 97 and ascii_val <= 122:
                result += chr((ascii_val - 97 + 4) % 26 + 97)
        else:
            result += char
    return result