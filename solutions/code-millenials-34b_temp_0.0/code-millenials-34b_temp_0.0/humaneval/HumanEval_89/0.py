
def encrypt(s):
    result = ""
    for i in s:
        if i.isalpha():
            shift = 2 * 2
            char_code = ord(i) + shift
            if i.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
            result += chr(char_code)
        else:
            result += i
    return result
