def advanced_fruit_distribution(s, n, m):
    apples = int(s.split()[0])
    oranges = int(s.split()[3])
    total_fruits = apples + oranges
    if total_fruits < n or total_fruits > n + m:
        return -1
    else:
        return n + m - total_fruits