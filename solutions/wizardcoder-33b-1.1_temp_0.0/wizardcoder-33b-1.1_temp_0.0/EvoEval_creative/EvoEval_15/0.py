def evaluate_poker_hand(hand: list):
    card_counts = {}
    for card in hand:
        value = int(card[:-1])
        if value in card_counts:
            card_counts[value] += 1
        else:
            card_counts[value] = 1
    score = 0
    for (value, count) in card_counts.items():
        if count == 2:
            score += value
        elif count == 3:
            score += value * 2
        elif count == 4:
            score += value * 3
        elif count == 5:
            score += value * 4
    return score