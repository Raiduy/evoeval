
def is_bored(S):
    sentences = S.split('.')
    sentences += S.split('?')
    sentences += S.split('!')
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith('I'):
            count += 1
    return count