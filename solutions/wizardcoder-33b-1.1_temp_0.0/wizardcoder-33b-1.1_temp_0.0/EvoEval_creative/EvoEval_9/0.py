
def calculate_word_frequency(s: str) -> dict:
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.lower()
    words = s.split()
    word_frequency = defaultdict(int)
    for word in words:
        word_frequency[word] += 1
    return word_frequency