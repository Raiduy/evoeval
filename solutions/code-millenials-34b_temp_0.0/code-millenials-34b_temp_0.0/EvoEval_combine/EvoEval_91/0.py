
def sort_prime_even(l, x, y):
    even_list = sorted([l[i] for i in range(0, len(l), 2)])
    for i in range(0, len(l), 2):
        if is_prime(even_list[i // 2]):
            even_list[i // 2] = x
        else:
            even_list[i // 2] = y
    for i in range(1, len(l), 2):
        even_list.insert(i, l[i])
    return even_list