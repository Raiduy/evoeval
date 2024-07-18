
def make_a_pile(n):
    pile = [n]
    while n > 1:
        if n % 2 == 0:
            n -= 2
        else:
            n -= 1
        pile.append(n)
    return pile[::-1]