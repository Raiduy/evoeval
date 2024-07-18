def how_many_times(string: str, substrings: list) -> dict:
    if not substrings:
        return 'Substrings cannot be empty'
    if not string:
        return {substring: 0 for substring in substrings}
    counts = {substring: 0 for substring in substrings}
    for substring in substrings:
        if not substring:
            return 'Substrings cannot be empty'
        count = 0
        start = 0
        while start < len(string):
            pos = string.find(substring, start)
            if pos != -1:
                count += 1
                start = pos + 1
            else:
                break
        counts[substring] = count
    return counts