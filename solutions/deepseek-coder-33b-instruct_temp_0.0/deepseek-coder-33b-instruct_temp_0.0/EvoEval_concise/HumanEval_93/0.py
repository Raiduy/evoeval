
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
    result = ''
    for char in message:
        if char in vowels:
            if char.islower():
                result += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        elif char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result