def advanced_fruit_distribution(s, n, m):
    numbers = re.findall('\\d+', s)
    apples = int(numbers[0])
    oranges = int(numbers[1])
    mangoes = n - (apples + oranges)
    if mangoes >= m:
        return mangoes
    else:
        return -1