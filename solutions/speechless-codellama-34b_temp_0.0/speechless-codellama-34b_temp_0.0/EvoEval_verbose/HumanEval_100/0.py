
def make_a_pile(n):
    pile = [n]
    while True:
        if n % 2 == 0:
            n += 2
        else:
            n += 2
        pile.append(n)
        if n > 1000:
            break
    return pile