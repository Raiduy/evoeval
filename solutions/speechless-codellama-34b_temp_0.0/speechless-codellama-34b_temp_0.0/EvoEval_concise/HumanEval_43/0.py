

def pairs_sum_to_zero(l):
    """
    Takes a list of integers (l) as input. Returns True if a pair of distinct elements sum to zero; otherwise, returns False.
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False