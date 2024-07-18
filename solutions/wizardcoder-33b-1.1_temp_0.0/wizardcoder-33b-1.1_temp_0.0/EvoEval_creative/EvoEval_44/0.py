def fairy_tale_transport(q, w, e):
    total_weight = sum(q)
    if total_weight <= w + e:
        return True
    else:
        return False