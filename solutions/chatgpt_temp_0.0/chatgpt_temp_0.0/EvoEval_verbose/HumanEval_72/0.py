
def will_it_fly(q, w):
    if q == q[::-1]:
        if sum(q) <= w:
            return True
    return False