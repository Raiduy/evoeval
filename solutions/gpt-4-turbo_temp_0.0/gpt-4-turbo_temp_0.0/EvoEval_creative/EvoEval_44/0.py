def fairy_tale_transport(q, w, e):
    total_weight = sum(q)
    combined_capacity = w + e
    if combined_capacity >= total_weight:
        return True
    else:
        return False