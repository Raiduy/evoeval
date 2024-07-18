def advanced_fruit_distribution(s, n, m):
    (apples, oranges) = map(int, s.split()[0::2])
    mangoes_needed = m - (n - apples - oranges)
    if mangoes_needed <= 0:
        return max(m, n - apples - oranges)
    else:
        max_mangoes = min(mangoes_needed, n - apples - oranges)
        if max_mangoes + apples + oranges < m:
            return -1
        else:
            return max_mangoes + apples + oranges