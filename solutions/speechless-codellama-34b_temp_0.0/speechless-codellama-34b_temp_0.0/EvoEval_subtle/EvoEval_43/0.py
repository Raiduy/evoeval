
def pairs_sum_to_one(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 1:
                return True
    return False