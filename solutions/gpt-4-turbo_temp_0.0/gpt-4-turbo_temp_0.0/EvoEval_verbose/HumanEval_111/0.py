
def histogram(test):
    letter_freq = {}
    for letter in test.replace(' ', ''):
        letter_freq[letter] = letter_freq.get(letter, 0) + 1
    max_freq = max(letter_freq.values(), default=0)
    max_freq_letters = {letter: freq for (letter, freq) in letter_freq.items() if freq == max_freq}
    return max_freq_letters