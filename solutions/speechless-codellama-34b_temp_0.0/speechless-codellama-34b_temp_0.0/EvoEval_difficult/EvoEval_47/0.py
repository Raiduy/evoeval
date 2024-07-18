def weighted_median(l: list, w: list):
    total_weight = sum(w)
    cumulative_weight = 0
    for i in range(len(l)):
        cumulative_weight += w[i]
        if cumulative_weight >= total_weight / 2:
            return l[i]
    return None