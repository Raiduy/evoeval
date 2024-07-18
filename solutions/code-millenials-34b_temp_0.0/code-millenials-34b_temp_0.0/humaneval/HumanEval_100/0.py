
def make_a_pile(n):
    stones = [n]
    for i in range(n-1):
        if n % 2 == 0:
            stones.append(n + 2*i)
        else:
            stones.append(n + 2*i)
    return stones
