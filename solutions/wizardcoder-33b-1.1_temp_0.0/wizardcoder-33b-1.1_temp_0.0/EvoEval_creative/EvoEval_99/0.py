def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    position = 0
    for round in rounds:
        position = (position + round * music) % len(players)
        players.pop(position)
    return players