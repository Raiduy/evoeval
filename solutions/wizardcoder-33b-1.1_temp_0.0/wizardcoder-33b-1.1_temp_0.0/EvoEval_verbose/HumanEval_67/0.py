
def fruit_distribution(s, n):
    words = s.split()
    num_apples = int(words[0])
    num_oranges = int(words[2])
    num_mangoes = n - (num_apples + num_oranges)
    return num_mangoes