
def histogram(test):
    frequency = {}
    for letter in test:
        if letter != ' ':
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    max_freq = max(frequency.values()) if frequency else 0
    return {key: value for (key, value) in frequency.items() if value == max_freq}