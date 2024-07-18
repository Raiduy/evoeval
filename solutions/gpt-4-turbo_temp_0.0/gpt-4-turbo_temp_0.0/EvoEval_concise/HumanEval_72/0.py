
def will_it_fly(q, w):
    is_palindromic = q == q[::-1]
    sum_within_limit = sum(q) <= w
    return is_palindromic and sum_within_limit