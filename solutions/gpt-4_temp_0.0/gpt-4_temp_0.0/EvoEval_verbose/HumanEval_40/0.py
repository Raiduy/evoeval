def triples_sum_to_zero(l: list) -> bool:
    triples = combinations(l, 3)
    for triple in triples:
        if sum(triple) == 0:
            return True
    return False