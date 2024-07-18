
def cycpattern_check(a, b):
    cyclic_permutations = [b[i:] + b[:i] for i in range(len(b))]
    for permutation in cyclic_permutations:
        if permutation in a:
            return True
    return False