
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
    vowels = 'aeiouAEIOU'
    vowel_replacement = 'cigkmoCIGKMO'
    translation_table = str.maketrans(vowels, vowel_replacement)
    return message.swapcase().translate(translation_table)