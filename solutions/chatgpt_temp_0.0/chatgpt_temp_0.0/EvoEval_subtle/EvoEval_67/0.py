def fruit_distribution(s, n):
    fruits = s.split(', ')
    total_fruits = n + 1
    apples = int(fruits[0].split()[0])
    oranges = int(fruits[1].split()[0])
    mangoes = total_fruits - apples - oranges
    return mangoes