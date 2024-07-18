
def histogram(test):
    hist = {}
    words = test.split()
    for word in words:
        for char in word:
            if char in hist:
                hist[char] += 1
            else:
                hist[char] = 1
    max_count = max(hist.values())
    max_hist = {char: count for (char, count) in hist.items() if count == max_count}
    return max_hist