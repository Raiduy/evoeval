
def anti_shuffle(s):

    def sort_word(word):
        return ''.join(sorted(word, key=lambda x: ord(x)))
    words = s.split()
    sorted_words = [sort_word(word) for word in words]
    return ' '.join(sorted_words)