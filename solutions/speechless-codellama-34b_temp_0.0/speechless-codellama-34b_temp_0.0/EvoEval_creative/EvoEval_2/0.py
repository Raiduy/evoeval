from typing import List, Union

def encrypt_message(words: List[str], key: Union[str, int]) -> List[Union[str, int]]:
    result = []
    for word in words:
        new_word = ''
        for char in word:
            if char.isalpha():
                shifted_char = chr((ord(char.lower()) - 96 + key) % 26 + 97)
                new_word += shifted_char
            else:
                new_word += char
        result.append(new_word)
    return result