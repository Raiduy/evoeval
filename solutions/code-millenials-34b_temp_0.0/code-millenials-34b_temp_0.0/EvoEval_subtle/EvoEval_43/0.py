
def pairs_sum_to_one(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False