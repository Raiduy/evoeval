
def is_bored(S):
    sentences = [s.strip() for s in S.split('.') if s.strip() != '']
    sentences += [s.strip() for s in S.split('?') if s.strip() != '']
    sentences += [s.strip() for s in S.split('!') if s.strip() != '']
    count = sum((1 for s in sentences if s.startswith('I ')))
    return count