
def sort_prime_even(l: list, x, y):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = sorted([l[i] for i in even_indices])
    for i in range(len(l)):
        if i % 2 == 0:
            if even_values[0] % 2 == 0:
                l[i] = x
            else:
                l[i] = y
            even_values.pop(0)
    return l