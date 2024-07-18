
def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 0 and words[0] == 'I':
            count += 1
    return count
