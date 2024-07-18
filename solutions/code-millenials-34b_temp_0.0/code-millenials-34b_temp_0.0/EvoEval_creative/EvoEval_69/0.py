def magicTrick(cards, magicNumber):
    card_dict = {}
    for (i, num) in enumerate(cards):
        if magicNumber / num in card_dict:
            return (card_dict[magicNumber / num], i)
        card_dict[num] = i
    return 'No magic today'