def vowels_count(s):
    vowels = 'aeiou'
    count = 0
    for letter in s:
        if letter.lower() in vowels:
            count += 1
        elif letter == 'y' and s.index(letter) == len(s) - 1:
            count += 1
    return count