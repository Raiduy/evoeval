
def select_words(s, n):
    vowels = set("aeiouAEIOU")
    words = s.split()
    result = []
    for word in words:
        if sum(1 for c in word if c not in vowels) == n:
            result.append(word)
    return result
