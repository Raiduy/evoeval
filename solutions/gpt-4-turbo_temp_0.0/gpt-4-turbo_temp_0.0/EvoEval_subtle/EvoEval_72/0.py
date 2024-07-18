
def will_it_fly(q, w):
    is_balanced = q == q[::-1]
    sum_of_elements = sum(q)
    is_sum_even = sum_of_elements % 2 == 0
    is_under_weight = sum_of_elements <= w
    return is_balanced and is_sum_even and is_under_weight