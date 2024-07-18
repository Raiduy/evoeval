
def fruit_distribution(s, n):
    s_list = s.split()
    num_apples = int(s_list[0])
    num_oranges = int(s_list[3])
    num_mango = n - num_apples - num_oranges
    return num_mango