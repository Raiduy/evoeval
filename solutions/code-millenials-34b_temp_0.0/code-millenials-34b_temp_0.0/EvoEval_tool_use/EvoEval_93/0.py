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
    words = sentence.split(' ')
    scrambled_words = []
    for word in words:
        if len(word) < 4:
            scrambled_words.append(word)
            continue
        second_char = word[1]
        second_last_char = word[-2]
        word = list(word)
        (word[1], word[-2]) = (word[-2], word[1])
        scrambled_words.append(''.join(word))
    return ' '.join(scrambled_words)