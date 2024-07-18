
def pile_median(n):
    pile = []
    for i in range(n):
        if n % 2 == 0:
            pile.append(n + 2 * i)
        else:
            pile.append(n + 2 * i)
    pile.sort()
    if n % 2 == 0:
        return (pile[n // 2 - 1] + pile[n // 2]) / 2
    else:
        return pile[n // 2]