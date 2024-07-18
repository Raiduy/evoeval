def fruit_distribution(s, n):
    s_list = s.split()
    apples = int(s_list[0])
    oranges = int(s_list[3])
    mango_fruits = n + 1 - apples - oranges
    return mango_fruits