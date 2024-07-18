def fruit_distribution(s, n):
    words = s.split()
    apples = int(words[0])
    oranges = int(words[2])
    mangoes = n - apples - oranges - 1
    return mangoes