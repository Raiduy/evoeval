from typing import List, Union

def encrypt_message(words: List[str], key: Union[str, int]) -> List[Union[str, int]]:
    if isinstance(key, str):
        key = sum((ord(c) for c in key))
    encrypted_words = []
    for word in words:
        encrypted_word = ''
        for char in word.lower():
            if 'a' <= char <= 'z':
                encrypted_word += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted_word += char
        encrypted_words.append(encrypted_word)
    return encrypted_words