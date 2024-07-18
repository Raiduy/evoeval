
def is_bored(S):
    sentences = re.split('[.!?]', S)
    count = 0
    for sentence in sentences:
        if sentence.strip().startswith('I') and sentence.strip().endswith('boredom'):
            count += 1
    return count