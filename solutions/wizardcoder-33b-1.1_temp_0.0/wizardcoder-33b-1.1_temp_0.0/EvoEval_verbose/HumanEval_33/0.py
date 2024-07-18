

def sort_third(l: list):
    divisible_by_3 = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_3.sort()
    l_prime = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime[i] = divisible_by_3.pop(0)
    return l_prime