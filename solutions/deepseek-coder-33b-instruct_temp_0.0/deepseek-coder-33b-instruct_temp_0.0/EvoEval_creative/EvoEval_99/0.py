def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    position = 0
    for r in rounds:
        position = (position + r * music) % len(players)
        players.pop(position)
    return players