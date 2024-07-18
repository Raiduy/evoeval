
def split_words(txt):
    words_by_space = txt.split()
    if len(words_by_space) > 1:
        return words_by_space
    words_by_comma = txt.split(',')
    if len(words_by_comma) > 1:
        return words_by_comma
    odd_position_count = 0
    for char in txt:
        if char.islower():
            if (ord(char) - ord('a')) % 2 == 1:
                odd_position_count += 1
    return odd_position_count