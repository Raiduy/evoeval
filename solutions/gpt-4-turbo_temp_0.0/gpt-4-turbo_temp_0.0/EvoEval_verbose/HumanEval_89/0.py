
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = 4
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result