
def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum((1 for (i, c) in enumerate(txt) if c.islower() and (ord(c) - ord('a')) % 2 == 1))