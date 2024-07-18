def evaluate_poker_hand(hand: list):
    card_freq = {}
    for card in hand:
        value = card[:-1]
        if value.isdigit():
            value = int(value)
        if value not in card_freq:
            card_freq[value] = 0
        card_freq[value] += 1
    score = 0
    for (value, freq) in card_freq.items():
        if freq == 2:
            score += value
        elif freq == 3:
            score += 2 * value
        elif freq == 4:
            score += 3 * value
        elif freq == 5:
            score += 4 * value
    return score