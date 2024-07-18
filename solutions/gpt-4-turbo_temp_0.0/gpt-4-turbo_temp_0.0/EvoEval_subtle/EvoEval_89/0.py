
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shifted = (ord(char) - ord('a') - 4) % 26
            result += chr(shifted + ord('a'))
        else:
            result += char
    return result