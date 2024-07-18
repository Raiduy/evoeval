
def will_it_fly(q, w):
    if q != q[::-1]:
        return False
    if sum(q) % 2 != 0 or sum(q) > w:
        return False
    return True