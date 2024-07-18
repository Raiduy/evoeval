

def sort_third(l: list):
    l_prime = l.copy()
    divisible_by_three_elements = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_three_elements_sorted = sorted(divisible_by_three_elements)
    sorted_index = 0
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime[i] = divisible_by_three_elements_sorted[sorted_index]
            sorted_index += 1
    return l_prime