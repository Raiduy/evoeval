def detect_boredom(S, substrings):
    count = 0
    sentences = re.split('[\\.\\?!]', S)
    for sentence in sentences:
        if any((sentence.strip().startswith(substring) for substring in substrings)):
            count += 1
    return count