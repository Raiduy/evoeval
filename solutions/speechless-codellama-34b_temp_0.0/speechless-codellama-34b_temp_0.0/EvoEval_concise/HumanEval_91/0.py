
def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if '?' in sentence or '!' in sentence:
            words = sentence.split(' ')
            if words[0] == 'I':
                count += 1
    return count