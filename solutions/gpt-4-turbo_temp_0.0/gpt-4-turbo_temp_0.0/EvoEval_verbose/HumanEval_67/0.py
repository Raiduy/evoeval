
def fruit_distribution(s, n):
    parts = s.split()
    num_apples = int(parts[0])
    num_oranges = int(parts[3])
    num_mangoes = n - (num_apples + num_oranges)
    return num_mangoes