

def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 3 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'THST'
    >>> encode('This is a message')
    'tHLS LS D MHSSDGH'
    """
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            new_char = chr((ord(char.lower()) - 97 + 3) % 26 + 97)
            if char.isupper():
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
            encoded_message += new_char
        elif char.isupper():
            encoded_message += char.lower()
        else:
            encoded_message += char.upper()
    return encoded_message