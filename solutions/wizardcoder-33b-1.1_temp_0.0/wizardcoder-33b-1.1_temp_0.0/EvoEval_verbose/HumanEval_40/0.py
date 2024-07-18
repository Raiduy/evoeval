def triples_sum_to_zero(l: list):
    if len(l) < 3:
        return False
    for triple in combinations(l, 3):
        if sum(triple) == 0:
            return True
    return False