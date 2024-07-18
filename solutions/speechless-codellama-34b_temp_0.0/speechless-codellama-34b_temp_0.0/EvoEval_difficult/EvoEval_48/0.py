def is_palindrome_sentence(sentence: str) -> bool:
    sentence = sentence.replace(' ', '').lower()
    sentence = ''.join((e for e in sentence if e.isalnum()))
    return sentence == sentence[::-1]