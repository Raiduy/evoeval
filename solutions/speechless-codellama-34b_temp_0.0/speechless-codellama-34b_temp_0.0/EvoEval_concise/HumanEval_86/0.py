
def anti_shuffle(s):
    words = s.split()
    sorted_words = [sorted(word) for word in words]
    sorted_s = ' '.join(sorted_words)
    return sorted_s