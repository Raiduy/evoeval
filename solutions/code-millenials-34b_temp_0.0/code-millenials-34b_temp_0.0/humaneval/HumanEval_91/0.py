
def is_bored(S):
    # Split the string into sentences
    sentences = []
    temp_sentence = ''
    for char in S:
        if char not in '.?!':
            temp_sentence += char
        else:
            sentences.append(temp_sentence.strip())
            temp_sentence = ''
    sentences.append(temp_sentence.strip())  # Append the last sentence

    # Count the number of boredoms
    boredom_count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            boredom_count += 1

    return boredom_count
