def magical_staircase(n: int, magic_stones: list):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        for stone in magic_stones:
            if i >= stone:
                ways[i] += ways[i - stone]
    return ways[n]