
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(n)]
    count = 0
    mod_count = [0] * 3
    for num in a:
        mod_count[num % 3] += 1
    count += mod_count[0] * (mod_count[0] - 1) * (mod_count[0] - 2) // 6
    count += mod_count[1] * mod_count[2]
    count += mod_count[0] * (mod_count[1] - 1) // 2 * mod_count[2]
    return count