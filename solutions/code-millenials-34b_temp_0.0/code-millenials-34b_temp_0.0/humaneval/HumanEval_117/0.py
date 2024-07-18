
def select_words(s, n):
    if s == "":
        return []
    else:
        words = s.split()
        consonants = "bcdfghjklmnpqrstvwxyz"
        selected_words = []
        for word in words:
            count = 0
            for letter in word:
                if letter.lower() in consonants:
                    count += 1
            if count == n:
                selected_words.append(word)
        return selected_words
