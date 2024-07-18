
def encode(message):
    """
    Swap case of all letters in the given message. Additionally, replace all vowels with the letter that's 2 places 
    ahead in the alphabet. Assume input contains only letters.
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowel_replacement = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = ''
    for char in message:
        if char in vowel_replacement:
            encoded_char = vowel_replacement[char]
        else:
            encoded_char = char
        encoded_message += encoded_char.swapcase()
    return encoded_message