def weighted_median(l: list, w: list):
    combined = list(zip(l, w))
    combined.sort()
    total_weight = sum(w)
    half_weight = total_weight / 2
    weight_sum = 0
    for (item, weight) in combined:
        weight_sum += weight
        if weight_sum >= half_weight:
            return item
    return None