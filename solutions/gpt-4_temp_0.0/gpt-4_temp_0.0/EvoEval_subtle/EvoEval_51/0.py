
def remove_consonants(text):
    """
    remove_consonants is a function that takes string and returns string without consonants.
    >>> remove_consonants('')
    ''
    >>> remove_consonants("abcdef
ghijklm")
    'ae
i'
    >>> remove_consonants('abcdef')
    'ae'
    >>> remove_consonants('aaaaa')
    'aaaaa'
    >>> remove_consonants('aaBAA')
    'aaAA'
    >>> remove_consonants('zbcd')
    ''
    """
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return ''.join((char for char in text if char not in consonants))