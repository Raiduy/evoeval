def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    position = 0
    for round_time in rounds:
        position += round_time * music - 1
        position %= len(players)
        players.pop(position)
    return players