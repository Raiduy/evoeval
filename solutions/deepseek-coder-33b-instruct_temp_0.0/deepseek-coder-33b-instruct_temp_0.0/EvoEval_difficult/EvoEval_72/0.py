def will_it_fly_advanced(q, w, r):
    q_removed = [q[i] for i in range(len(q)) if i not in r]
    is_palindrome = q_removed == q_removed[::-1]
    sum_q = sum(q_removed)
    is_weight_ok = sum_q <= w
    if is_palindrome and is_weight_ok:
        return True
    elif not is_palindrome:
        return False
    else:
        return None