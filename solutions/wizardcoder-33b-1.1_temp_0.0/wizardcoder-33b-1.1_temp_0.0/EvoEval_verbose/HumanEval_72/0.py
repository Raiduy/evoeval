
def will_it_fly(q, w):
    is_palindromic = q == q[::-1]
    total_weight = sum(q)
    can_fly = total_weight <= w
    return is_palindromic and can_fly