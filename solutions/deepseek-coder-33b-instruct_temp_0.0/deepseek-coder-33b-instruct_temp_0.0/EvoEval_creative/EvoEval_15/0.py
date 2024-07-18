def evaluate_poker_hand(hand: list):
    """ 
    Evaluate a poker hand and return its score.

    In this game, we use the following point scoring rules:

    1. Each card has a value (A=1, 2-10 = card number, J=11, Q=12, K=13)
    2. A 'pair' (two cards of the same value) scores the value of the card.
    3. A 'triple' (three cards of the same value) scores double the value of the card.
    4. A 'four of a kind' (four cards of the same value) scores triple the value of the card.
    5. A 'five of a kind' (five cards of the same value) scores quadruple the value of the card.
    6. If hand has no pairs, triples or fours, score is 0

    Note, you should consider all cards in hand, i.e., if there are both pair and triple, score should be score or pair + score of triple.

    The "hand" list contains 5 strings, each representing a card in the format 'value+suit'
    (i.e. ['10H', '10D', '10C', '2S', '2D']). The suit is irrelevant for this game.

    >>> evaluate_poker_hand(['5H', '5D', '5S', '9C', '9D'])
    19
    >>> evaluate_poker_hand(['AS', '2H', '3S', '4H', '5D'])
    0
    >>> evaluate_poker_hand(['KH', 'KD', 'KS', 'KC', 'KA'])
    52
    """
    card_counts = {}
    for card in hand:
        value = card[:-1]
        if value in card_counts:
            card_counts[value] += 1
        else:
            card_counts[value] = 1
    score = 0
    for count in card_counts.values():
        if count == 2:
            score += int(value) * 2
        elif count == 3:
            score += int(value) * 3
        elif count == 4:
            score += int(value) * 4
        elif count == 5:
            score += int(value) * 5
    return score