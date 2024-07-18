def will_it_fly_advanced(q, w, r):
    q_new = [q[i] for i in range(len(q)) if i not in r]
    if q_new != q_new[::-1]:
        return False
    if sum(q_new) > w:
        return None
    return True