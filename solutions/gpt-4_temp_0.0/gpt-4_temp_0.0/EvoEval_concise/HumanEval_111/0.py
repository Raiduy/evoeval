
def histogram(test):
    """Return a dictionary with keys as letters from a given string of space separated lowercase letters and values being their counts. If multiple letters have the same maximum frequency, include them all.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    letters = test.split()
    counts = {}
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values(), default=0)
    max_counts = {letter: count for (letter, count) in counts.items() if count == max_count}
    return max_counts