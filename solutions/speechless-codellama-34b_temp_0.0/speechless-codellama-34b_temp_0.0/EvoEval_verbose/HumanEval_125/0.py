
def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return [word.strip(',') for word in txt.split(',')]
    else:
        count = 0
        for letter in txt:
            if letter.islower() and (ord(letter) - ord('a')) % 2 == 1:
                count += 1
        return count