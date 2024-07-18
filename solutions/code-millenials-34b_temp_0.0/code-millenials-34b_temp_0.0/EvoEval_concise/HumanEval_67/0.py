
def fruit_distribution(s, n):
    apples = int(s.split(' apples')[0])
    oranges = int(s.split(' oranges')[0].split(' and ')[1])
    mangoes = n - (apples + oranges)
    return mangoes