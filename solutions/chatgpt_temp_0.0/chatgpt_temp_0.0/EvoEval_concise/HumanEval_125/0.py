
def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for i in range(len(txt)):
            if i % 2 == 1 and txt[i].islower():
                count += 1
        return count