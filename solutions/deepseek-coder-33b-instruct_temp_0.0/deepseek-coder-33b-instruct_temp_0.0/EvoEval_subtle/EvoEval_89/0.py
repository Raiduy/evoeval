
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
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + 2 * 2 - 26) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result