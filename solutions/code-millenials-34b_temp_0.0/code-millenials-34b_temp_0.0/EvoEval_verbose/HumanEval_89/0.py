
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = 4
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                start = ord('A')
                result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result