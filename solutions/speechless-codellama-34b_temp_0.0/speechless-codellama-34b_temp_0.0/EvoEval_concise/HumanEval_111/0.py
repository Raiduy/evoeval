
def histogram(test):
    letters = test.split()
    counts = {}
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values())
    max_count_letters = {}
    for (letter, count) in counts.items():
        if count == max_count:
            max_count_letters[letter] = count
    return max_count_letters