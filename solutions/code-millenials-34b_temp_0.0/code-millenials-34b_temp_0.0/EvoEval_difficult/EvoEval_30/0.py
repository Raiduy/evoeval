def get_positive_and_index(l):
    result = []
    for (i, val) in enumerate(l):
        if val > 0 and is_prime(i):
            result.append((val, i))
    return result