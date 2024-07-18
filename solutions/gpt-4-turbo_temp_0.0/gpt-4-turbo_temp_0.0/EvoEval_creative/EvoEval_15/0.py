def evaluate_poker_hand(hand: list):
    value_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    value_counts = {}
    for card in hand:
        value = card[:-1]
        numerical_value = value_map[value]
        if numerical_value in value_counts:
            value_counts[numerical_value] += 1
        else:
            value_counts[numerical_value] = 1
    score = 0
    for (value, count) in value_counts.items():
        if count == 2:
            score += value
        elif count == 3:
            score += value * 2
        elif count == 4:
            score += value * 3
        elif count == 5:
            score += value * 4
    return score