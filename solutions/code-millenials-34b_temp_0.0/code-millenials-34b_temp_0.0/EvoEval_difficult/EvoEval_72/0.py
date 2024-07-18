def will_it_fly_advanced(q, w, r):

    def is_palindrome(lst):
        return lst == lst[::-1]
    q_without_r = [v for (i, v) in enumerate(q) if i not in r]
    if is_palindrome(q_without_r):
        if sum(q_without_r) <= w:
            return True
        else:
            return None
    else:
        return False