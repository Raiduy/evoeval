def evaluate_poker_hand(hand: list):
    values = [card[:-1] for card in hand]
    counts = [values.count(value) for value in set(values)]
    score = 0
    for count in counts:
        if count == 2:
            score += int(hand[values.index(values[counts.index(count)])][:-1])
        elif count == 3:
            score += 2 * int(hand[values.index(values[counts.index(count)])][:-1])
        elif count == 4:
            score += 3 * int(hand[values.index(values[counts.index(count)])][:-1])
        elif count == 5:
            score += 4 * int(hand[values.index(values[counts.index(count)])][:-1])
    return score