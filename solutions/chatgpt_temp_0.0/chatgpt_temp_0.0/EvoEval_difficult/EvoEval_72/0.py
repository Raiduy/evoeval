def will_it_fly_advanced(q, w, r):
    if q == q[::-1]:
        if sum(q) <= w:
            if q == [q[i] for i in range(len(q)) if i not in r]:
                return True
            else:
                return None
        else:
            return False
    else:
        return False