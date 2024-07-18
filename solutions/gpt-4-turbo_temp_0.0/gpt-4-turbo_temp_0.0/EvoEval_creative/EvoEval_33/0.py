def magical_staircase(n: int, magic_stones: list) -> int:
    ways = [0] * (n + 1)
    ways[0] = 1
    for step in range(1, n + 1):
        for stone in magic_stones:
            if step - stone >= 0:
                ways[step] += ways[step - stone]
    return ways[n]