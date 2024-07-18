from typing import List, Union

def encrypt_message(words: List[str], key: Union[str, int]) -> List[Union[str, int]]:
    """
    Given a list of words, first turn words into lowercase and then encrypt each word using a simple Caesar cipher. 
    The key for the cipher is either a string or an integer.
    If the key is a string, convert it to an integer by summing the ASCII values 
    of its characters. If the key is an integer, use it as-is.

    The Caesar cipher works by shifting each letter in the word by the 
    value of the key. If the letter after shifting exceeds 'z', it wraps 
    around to the start of the alphabet.

    If the word contains any non-alphabetical characters, leave them as-is.
    """
    if isinstance(key, str):
        key = sum((ord(char) for char in key))
    encrypted_words = []
    for word in words:
        encrypted_word = ''
        for char in word.lower():
            if char.isalpha():
                shifted_char = chr((ord(char) - 97 + key) % 26 + 97)
                encrypted_word += shifted_char
            else:
                encrypted_word += char
        encrypted_words.append(encrypted_word)
    return encrypted_words