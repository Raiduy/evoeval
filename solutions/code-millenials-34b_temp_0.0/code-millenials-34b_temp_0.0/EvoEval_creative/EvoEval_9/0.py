
def calculate_word_frequency(string: str) -> dict:
    string = re.sub('[^\\w\\s]', '', string).lower()
    words = string.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency