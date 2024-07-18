
def histogram(test):
    freq = {}
    letters = test.split()
    for letter in letters:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    max_freq = max(freq.values())
    max_freq_letters = {}
    for (letter, freq) in freq.items():
        if freq == max_freq:
            max_freq_letters[letter] = freq
    return max_freq_letters