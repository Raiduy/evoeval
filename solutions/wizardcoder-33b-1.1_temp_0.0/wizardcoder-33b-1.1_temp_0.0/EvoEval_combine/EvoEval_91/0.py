
def sort_prime_even(l, x, y):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    for i in range(len(even_indices)):
        if is_prime(even_indices[i]):
            even_indices[i] = x
        else:
            even_indices[i] = y
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = even_indices.pop(0)
    return l