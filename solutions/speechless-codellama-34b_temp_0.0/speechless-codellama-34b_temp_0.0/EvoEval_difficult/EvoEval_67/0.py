def advanced_fruit_distribution(s, n, m):
    s_list = s.split()
    num_apples = 0
    num_oranges = 0
    for i in range(len(s_list)):
        if s_list[i] == 'apples':
            num_apples = int(s_list[i - 1])
        elif s_list[i] == 'oranges':
            num_oranges = int(s_list[i - 1])
    total_fruits = num_apples + num_oranges
    if total_fruits < m:
        return -1
    else:
        return n - total_fruits