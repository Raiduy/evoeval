def evaluate_poker_hand(hand: list):
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    card_values = [values[card[:-1]] for card in hand]
    card_counts = {value: card_values.count(value) for value in set(card_values)}
    score = 0
    for (value, count) in card_counts.items():
        if count == 2:
            score += value
        elif count == 3:
            score += 2 * value
        elif count == 4:
            score += 3 * value
        elif count == 5:
            score += 4 * value
    return score