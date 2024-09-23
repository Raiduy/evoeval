def detect_boredom(S, substrings):
    count = 0
    S = re.sub('\\(.*?\\)|\\[.*?\\]|{.*?}|".*?"', '', S)
    sentences = re.split('[.!?]', S)
    for sentence in sentences:
        sentence = sentence.strip()
        for substring in substrings:
            if sentence.startswith(substring):
                count += 1
                break
    return count