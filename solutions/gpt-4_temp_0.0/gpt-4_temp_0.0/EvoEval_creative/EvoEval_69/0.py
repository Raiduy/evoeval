def magicTrick(cards, magicNumber):
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if cards[i] * cards[j] == magicNumber:
                return (i, j)
    return 'No magic today'