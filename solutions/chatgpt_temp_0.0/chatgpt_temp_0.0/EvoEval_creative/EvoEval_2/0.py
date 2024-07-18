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

    >>> encrypt_message([], "abc")
    []
    >>> encrypt_message(["hello", "world"], 3)
    ["khoor", "zruog"]
    >>> encrypt_message(["hello", "world"], "abc")
    ["pmttw", "ewztl"]
    """

    def caesar_cipher(word, shift):
        encrypted_word = ''
        for char in word:
            if char.isalpha():
                shift_amount = ord(key) - ord('a') if isinstance(key, str) else key
                shifted_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
                encrypted_word += shifted_char if char.islower() else shifted_char.upper()
            else:
                encrypted_word += char
        return encrypted_word
    key = sum((ord(char) for char in str(key))) if isinstance(key, str) else key
    return [caesar_cipher(word.lower(), key) for word in words]