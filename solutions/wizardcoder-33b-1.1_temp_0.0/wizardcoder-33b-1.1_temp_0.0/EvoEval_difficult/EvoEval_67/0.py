def advanced_fruit_distribution(s, n, m):
    words = s.split()
    apples = int(words[0])
    oranges = int(words[2])
    mangoes = n - apples - oranges
    if mangoes < m:
        return -1
    else:
        return mangoes