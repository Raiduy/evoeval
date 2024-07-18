
def histogram(test):
    """Return a dictionary with keys as letters from a given string of space separated lowercase letters and values being their counts. If multiple letters have the same maximum frequency, include them all.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    letters = [letter for letter in test.split(' ') if letter]
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    max_freq = max(letter_counts.values(), default=0)
    max_freq_letters = {letter: count for (letter, count) in letter_counts.items() if count == max_freq}
    return max_freq_letters