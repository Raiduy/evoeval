import string

def is_valid(word):
    valid_chars = string.ascii_letters + ' '
    for char in word:
        if char not in valid_chars:
            return False
    return True
def scramble(sentence):
    if not is_valid(sentence):
        return ''
    words = sentence.split()
    scrambled_words = []
    for word in words:
        if len(word) >= 4:
            chars = list(word)
            second_char = chars[1]
            second_last_char = chars[-2]
            (chars[1], chars[-2]) = (second_last_char, second_char)
            scrambled_word = ''.join(chars)
            scrambled_words.append(scrambled_word)
        else:
            scrambled_words.append(word)
    return ' '.join(scrambled_words)