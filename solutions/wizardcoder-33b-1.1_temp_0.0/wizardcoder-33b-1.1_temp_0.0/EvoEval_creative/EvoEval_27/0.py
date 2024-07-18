def split_strings(s: str, n: int):
    return [s[i:i + n] for i in range(0, len(s), n)]