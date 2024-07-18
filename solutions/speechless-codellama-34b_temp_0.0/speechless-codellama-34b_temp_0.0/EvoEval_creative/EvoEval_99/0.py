def musical_chairs(n, rounds, music):
    players = list(range(1, n + 1))
    for round_time in rounds:
        for _ in range(round_time):
            players.insert(0, players.pop())
        players.pop(0)
    return players