
def histogram(test):
    """Return a dictionary with keys as letters from a given string of space separated lowercase letters and values being their counts. If multiple letters have the same maximum frequency, include them all.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    words = test.split()
    hist = {}
    for word in words:
        for letter in word:
            if letter in hist:
                hist[letter] += 1
            else:
                hist[letter] = 1
    max_count = max(hist.values()) if hist else 0
    max_hist = {k: v for (k, v) in hist.items() if v == max_count}
    return max_hist