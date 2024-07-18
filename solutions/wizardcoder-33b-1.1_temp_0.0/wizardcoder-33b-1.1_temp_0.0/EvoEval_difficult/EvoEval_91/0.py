def detect_boredom(S, substrings):
    placeholders = ['{}', '()', '[]']
    for p in placeholders:
        S = re.sub('\\{.*?\\}'.format(p), 'placeholder', S)
    S = re.sub('"[^"]*"', 'placeholder', S)
    S = re.sub("'[^']*'", 'placeholder', S)
    sentences = re.split('[.!?]', S)
    count = 0
    for sentence in sentences:
        for substring in substrings:
            if sentence.strip().startswith(substring):
                count += 1
                break
    return count