def will_it_fly_advanced(q, w, r):
    q = [q[i] for i in range(len(q)) if i not in r]
    if sum(q) > w:
        return False
    if q == q[::-1]:
        return True
    if r:
        return None
    return False