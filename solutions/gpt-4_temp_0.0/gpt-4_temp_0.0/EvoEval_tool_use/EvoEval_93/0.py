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
        else:
            word_list = list(word)
            (word_list[1], word_list[-2]) = (word_list[-2], word_list[1])
            scrambled_word = ''.join(word_list)
            scrambled_words.append(scrambled_word)
    return ' '.join(scrambled_words)