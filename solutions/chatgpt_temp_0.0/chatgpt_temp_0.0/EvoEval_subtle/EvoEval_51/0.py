
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonant_free_text = ''
    for char in text:
        if char.lower() in vowels:
            consonant_free_text += char
    return consonant_free_text