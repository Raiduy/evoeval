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
    """
    card_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    card_values.update({str(i): i for i in range(2, 11)})
    card_counts = {value: 0 for value in card_values.keys()}
    for card in hand:
        card_counts[card[:-1]] += 1
    score = 0
    for (card, count) in card_counts.items():
        if count == 2:
            score += card_values[card]
        elif count == 3:
            score += 2 * card_values[card]
        elif count == 4:
            score += 3 * card_values[card]
        elif count == 5:
            score += 4 * card_values[card]
    return score