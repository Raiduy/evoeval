
def make_a_pile(n):
    pile = [n]
    level = n
    while True:
        if level % 2 == 0:
            level += 2
        else:
            level += 2
        pile.append(level)
        if level >= 2 * n:
            break
    return pile