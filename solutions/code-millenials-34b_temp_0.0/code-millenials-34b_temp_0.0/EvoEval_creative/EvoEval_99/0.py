def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    position = 0
    for round_time in rounds:
        for _ in range(round_time):
            position = (position + music) % len(players)
            del players[position]
    return players