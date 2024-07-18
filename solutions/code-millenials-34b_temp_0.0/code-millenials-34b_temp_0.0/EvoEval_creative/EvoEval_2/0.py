from typing import List, Union

def encrypt_message(words: List[str], key: Union[str, int]) -> List[str]:

    def ascii_sum(s: str) -> int:
        return sum((ord(c) for c in s))

    def caesar_cipher(word: str, key: int) -> str:
        result = ''
        for c in word:
            if not c.isalpha():
                result += c
            else:
                start = ord('a') if c.islower() else ord('A')
                result += chr((ord(c) - start + key) % 26 + start)
        return result
    if isinstance(key, str):
        key = ascii_sum(key)
    return [caesar_cipher(word.lower(), key) for word in words]