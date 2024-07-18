
def histogram(test):
    """Return a dictionary with keys as letters from a given string of space separated lowercase letters and values being their counts. If multiple letters have the same maximum frequency, include them all.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    letter_counts = {}
    letters = test.split()
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    max_count = max(letter_counts.values())
    max_letters = {}
    for (letter, count) in letter_counts.items():
        if count == max_count:
            max_letters[letter] = count