def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    current_position = 0
    for round_duration in rounds:
        steps = round_duration * music % len(players)
        current_position = (current_position + steps) % len(players)
        players.pop(current_position)
        if current_position == len(players):
            current_position = 0
    return players