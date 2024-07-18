
def is_bored(S):
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    boredoms = [sentence for sentence in sentences if sentence.strip().startswith('I')]
    return len(boredoms)
