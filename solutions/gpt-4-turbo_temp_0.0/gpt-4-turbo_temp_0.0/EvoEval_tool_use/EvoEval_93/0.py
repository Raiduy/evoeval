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
    scrambled_sentence = []
    words = sentence.split(' ')
    for word in words:
        if len(word) < 4:
            scrambled_sentence.append(word)
        else:
            char_list = list(word)
            (char_list[1], char_list[-2]) = (char_list[-2], char_list[1])
            scrambled_sentence.append(''.join(char_list))
    return ' '.join(scrambled_sentence)