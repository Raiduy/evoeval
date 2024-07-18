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
    result = ''
    for char in text:
        if is_special_char(char) or is_digit(char):
            result += char
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)
    return result