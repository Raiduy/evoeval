def magical_staircase(n: int, magic_stones: list):
    ways = [0] * (n + 1)
    ways[0] = 1
    for power in magic_stones:
        for i in range(power, n + 1):
            ways[i] += ways[i - power]
    return ways[n]