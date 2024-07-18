def detect_boredom(S, substrings):
    pattern = '(?:(?<!\\(.*)|(?<!\\[.*)|(?<!\\{.*))(?:(?<!".*))(?:(?<!\\\'.*))[.!?]'
    sentences = re.split(pattern, S)
    boredom_count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if any((sentence.startswith(sub) for sub in substrings)):
            boredom_count += 1
    return boredom_count