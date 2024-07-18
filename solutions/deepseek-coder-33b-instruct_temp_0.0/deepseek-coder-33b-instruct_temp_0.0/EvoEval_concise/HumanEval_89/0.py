
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
            ascii_offset = 97 if char.islower() else 65
            encrypted_char = chr((ord(char) - ascii_offset + 4) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result