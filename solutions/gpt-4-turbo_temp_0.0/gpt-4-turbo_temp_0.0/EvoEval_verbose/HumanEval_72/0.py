
def will_it_fly(q, w):
    is_balanced = q == q[::-1]
    total_weight = sum(q)
    return is_balanced and total_weight <= w