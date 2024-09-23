
def encrypt(s):
    """Develop an encrypt function that accepts a string and returns it encrypted by rotating the alphabet four places down. 
    For instance:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = ''
    for char in s:
        if char.isalpha():
            shift = 4
            char_code = ord(char) + shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
            result += chr(char_code)
        else:
            result += char
    return result