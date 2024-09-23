
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift up by two multiplied to two places.
    For example:
    encrypt('lm') returns 'hi'
    encrypt('ewhjklnop') returns 'asdfghjkl'
    encrypt('kj') returns 'gf'
    encrypt('ix') returns 'et'
    """
    result = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - 4) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - 4) % 26 + 97)
        else:
            result += char
    return result