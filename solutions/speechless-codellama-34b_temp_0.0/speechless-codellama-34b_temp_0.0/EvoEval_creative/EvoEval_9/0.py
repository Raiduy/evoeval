
def calculate_word_frequency(string: str) -> dict:
    string = re.sub('[^\\w\\s]', '', string).lower()
    words = string.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq