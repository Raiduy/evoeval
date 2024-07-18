
def is_bored(S):
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith('I ') or sentence.startswith('I.'):
            count += 1
    return count