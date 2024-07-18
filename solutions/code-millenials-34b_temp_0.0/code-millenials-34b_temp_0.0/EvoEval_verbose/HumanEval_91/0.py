
def is_bored(S):
    termination_marks = ['.', '?', '!']
    boredom_count = 0
    start_index = 0
    for i in range(len(S)):
        if S[i] in termination_marks:
            next_word = S[i + 1:].lstrip(' ').split(' ')[0]
            if next_word == 'I':
                boredom_count += 1
            start_index = i + 1
    return boredom_count