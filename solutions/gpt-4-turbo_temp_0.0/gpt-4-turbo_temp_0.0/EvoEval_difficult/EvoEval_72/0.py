def will_it_fly_advanced(q, w, r):
    q_reduced = [q[i] for i in range(len(q)) if i not in r]

    def is_palindrome(lst):
        return lst == lst[::-1]
    if is_palindrome(q) and sum(q) <= w:
        return True
    elif sum(q_reduced) <= w:
        if not is_palindrome(q_reduced):
            return None
        else:
            return True
    return False