
def remove_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    no_consonants = ''
    for char in text:
        if char not in consonants:
            no_consonants += char
    return no_consonants