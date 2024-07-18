def is_palindrome_sentence(sentence: str):
    sentence = sentence.lower()
    sentence = ''.join((e for e in sentence if e.isalnum()))
    return sentence == sentence[::-1]