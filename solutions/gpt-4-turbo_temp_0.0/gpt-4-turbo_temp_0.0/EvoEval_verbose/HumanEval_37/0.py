

def sort_even(l: list) -> list:
    even_indices_elements = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices_elements.sort()
    l_prime = l[:]
    for i in range(0, len(l), 2):
        l_prime[i] = even_indices_elements.pop(0)
    return l_prime