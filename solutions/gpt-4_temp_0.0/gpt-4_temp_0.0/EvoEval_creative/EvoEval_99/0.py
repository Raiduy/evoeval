def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    for round in rounds:
        position = round * music % len(players)
        del players[position]
    return players