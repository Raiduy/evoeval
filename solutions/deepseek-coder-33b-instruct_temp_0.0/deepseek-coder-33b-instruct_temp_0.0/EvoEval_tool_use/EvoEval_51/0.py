def is_special_char(char):
    """
    is_special_char is a helper function that takes a character and checks if it is a special character.

    >>> is_special_char('a')
    False
    >>> is_special_char('!')
    True
    >>> is_special_char('1')
    False
    >>> is_special_char('&')
    True
    """
    special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?"
    return char in special_chars


def is_digit(char):
    """
    is_digit is a helper function that takes a character and checks if it is a digit.

    >>> is_digit('a')
    False
    >>> is_digit('1')
    True
    >>> is_digit('9')
    True
    >>> is_digit('&')
    False
    """
    return char.isdigit()
def encrypt_text(text, shift):
    """
    encrypt_text is a function that performs a Caesar Cipher encryption on the input string. It takes a string and an integer shift value,
    and returns a new string where each letter is shifted by the shift value. The function keeps the special characters ("!@#$%^&*()-_=+[]{};:'",.<>/?") and digit characters intact.

    Note: A Caesar Cipher works by shifting the letters in the alphabet by a certain amount. For example, with a shift of 1, 'a' becomes 'b', 'b' becomes 'c', etc.
    'z' would wrap around to become 'a'. The same applies for uppercase letters. 

    >>> encrypt_text('', 3)
    ''
    >>> encrypt_text('abcd', 1)
    'bcde'
    >>> encrypt_text('xyz', 2)
    'zab'
    >>> encrypt_text('Hello, World!', 5)
    'Mjqqt, Btwqi!'
    >>> encrypt_text('123abc!', 3)
    '123def!'
    """
    result = ''
    for char in text:
        if is_special_char(char) or is_digit(char):
            result += char
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)
    return result