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
        if len(word) < 4:
            scrambled_words.append(word)
        else:
            second_char = word[1]
            second_last_char = word[-2]
            middle_chars = word[2:-2]
            scrambled_word = word[0] + second_last_char + middle_chars + second_char + word[-1]
            scrambled_words.append(scrambled_word)
    return ' '.join(scrambled_words)