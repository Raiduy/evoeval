
def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 1 and words[0] == 'I' and (words[-1] == 'boredom'):
            count += 1
    return count