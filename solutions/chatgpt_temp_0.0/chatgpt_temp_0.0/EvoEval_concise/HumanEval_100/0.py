
def make_a_pile(n):
    pile = []
    stones = n
    for i in range(n):
        pile.append(stones)
        if n % 2 == 0:
            stones += 2
        else:
            stones += 2 if i % 2 == 0 else 1
    return pile