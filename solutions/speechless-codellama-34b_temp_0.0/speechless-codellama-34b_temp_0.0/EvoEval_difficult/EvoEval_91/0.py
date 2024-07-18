def detect_boredom(S, substrings):
    count = 0
    for substring in substrings:
        if substring in S:
            count += 1
    return count