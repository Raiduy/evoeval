

def sort_third(l: list):
    sorted_elements = sorted([l[i] for i in range(0, len(l), 3)])
    l_prime = l.copy()
    for (i, element) in enumerate(sorted_elements):
        l_prime[i * 3] = element
    return l_prime