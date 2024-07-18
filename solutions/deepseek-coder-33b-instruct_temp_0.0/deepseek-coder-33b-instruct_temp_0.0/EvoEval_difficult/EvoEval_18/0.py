def how_many_times(string: str, substrings: list) -> dict:
    for substring in substrings:
        if not substring:
            raise ValueError('Substring cannot be an empty string')
    counts = {substring: 0 for substring in substrings}
    if not string:
        return counts
    for substring in substrings:
        start = 0
        while start < len(string):
            pos = string.find(substring, start)
            if pos != -1:
                start = pos + 1
                counts[substring] += 1
            else:
                break
    return counts