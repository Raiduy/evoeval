
def is_bored(S):
    import re
    sentences = re.split('[.?!]', S)
    count = 0
    for sentence in sentences:
        stripped_sentence = sentence.strip()
        if stripped_sentence.startswith('I'):
            count += 1
    return count