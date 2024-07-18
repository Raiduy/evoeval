def detect_boredom(S, substrings):
    brackets = ['()', '[]', '{}', '""', "''"]
    for bracket in brackets:
        S = re.sub('\\{0}[^\\{0}]*\\(0'.format(bracket), '', S)
    sentences = re.split('[.?!]', S)
    boredoms = 0
    for sentence in sentences:
        for substring in substrings:
            if sentence.strip().startswith(substring):
                boredoms += 1
                break
    return boredoms