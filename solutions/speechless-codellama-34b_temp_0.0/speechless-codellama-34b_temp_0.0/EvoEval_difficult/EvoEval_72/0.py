def will_it_fly_advanced(q, w, r):
    if q != q[::-1]:
        return False
    for i in r:
        del q[i]
    if q != q[::-1]:
        return False
    if sum(q) <= w:
        return True
    else:
        return None