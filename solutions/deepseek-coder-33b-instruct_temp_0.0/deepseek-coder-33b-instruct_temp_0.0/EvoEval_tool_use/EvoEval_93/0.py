import string

def is_valid(word):
    valid_chars = string.ascii_letters + ' '
    for char in word:
        if char not in valid_chars:
            return False
    return True
def scramble(sentence):
    """
    Write a function that takes a sentence (a string), and returns a new string that has each word scrambled. 
    For each word in the sentence, the function should randomly swap second and second last characters in the word. 
    The characters to be swapped should NOT be the first or the last character of the word.
    
    If a word has less than 4 characters (i.e., it is impossible to swap any characters without affecting the 
    first or last character), it should be left as it is.

    Check if the sentence contains only valid characters (alphabets and spaces). 
    If not, the function should return an empty string.
    
    The function should keep the case of the letters intact.
    
    Assume that words in the sentence are separated by a single space.
    
    Examples:
    >>> scramble('Hello World')
    'Hlleo Wlrod'
    >>> scramble('Python programming')
    'Pothyn pnogrammirg'
    >>> scramble('Invalid, sentence')
    ''
    """
    if not is_valid(sentence):
        return ''
    words = sentence.split(' ')
    scrambled_words = []
    for word in words:
        if len(word) > 3:
            chars = list(word)
            second_char = chars[1]
            second_last_char = chars[-2]
            chars[1] = second_last_char
            chars[-2] = second_char
            word = ''.join(chars)
        scrambled_words.append(word)
    return ' '.join(scrambled_words)