def weighted_median(l: list, w: list):
    combined = sorted(zip(l, w), key=lambda x: x[0])
    total_weight = sum(w)
    cumulative_weight = 0
    for (i, (value, weight)) in enumerate(combined):
        cumulative_weight += weight
        if cumulative_weight * 2 == total_weight:
            if i + 1 < len(combined) and combined[i + 1][1] == weight:
                return (value + combined[i + 1][0]) / 2
            else:
                return combined[i + 1][0]
        elif cumulative_weight * 2 > total_weight:
            return value